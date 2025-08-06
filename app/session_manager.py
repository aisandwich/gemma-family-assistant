# session_manager.py - Manage up to 5 concurrent sessions with timeouts

import time
import streamlit as st
from datetime import datetime, timedelta
import hashlib
import os
import json

class SessionManager:
    def __init__(self, session_timeout_minutes=5, max_concurrent_users=5):
        """
        Manage multiple concurrent sessions with timeout
        """
        self.session_timeout = session_timeout_minutes * 60  # Convert to seconds
        self.max_users = max_concurrent_users
        self.sessions_file = "active_sessions.json"  # Changed to JSON for multiple users
        
    def get_session_id(self):
        """Generate unique session ID based on device fingerprint"""
        try:
            # Try to get real user info from Streamlit
            user_agent = st.context.headers.get('user-agent', 'unknown')
            forwarded_for = st.context.headers.get('x-forwarded-for', 'unknown')
            
            # Create more unique fingerprint
            import random
            import uuid
            
            # Include browser info, screen size, etc to differentiate devices
            device_info = f"{user_agent}_{forwarded_for}_{st.session_state.get('device_id', '')}"
            
            # If no device_id in session state, create one
            if 'device_id' not in st.session_state:
                st.session_state.device_id = str(uuid.uuid4())[:8]
            
            session_info = f"{device_info}_{st.session_state.device_id}"
            session_id = hashlib.md5(session_info.encode()).hexdigest()[:12]
            
            return session_id
            
        except Exception as e:
            # Fallback: random session ID
            if 'fallback_session_id' not in st.session_state:
                import random
                st.session_state.fallback_session_id = f"user_{random.randint(10000, 99999)}"
            return st.session_state.fallback_session_id
    
    def load_sessions(self):
        """Load all active sessions"""
        try:
            if os.path.exists(self.sessions_file):
                with open(self.sessions_file, 'r') as f:
                    sessions = json.load(f)
                    # Clean expired sessions
                    current_time = time.time()
                    active_sessions = {}
                    for session_id, session_data in sessions.items():
                        if current_time - session_data['last_activity'] < self.session_timeout:
                            active_sessions[session_id] = session_data
                    
                    # Save cleaned sessions back
                    self.save_sessions(active_sessions)
                    return active_sessions
            return {}
        except Exception:
            return {}
    
    def save_sessions(self, sessions):
        """Save sessions to file"""
        try:
            with open(self.sessions_file, 'w') as f:
                json.dump(sessions, f)
        except Exception:
            pass
    
    def check_session_access(self):
        """
        Check if current user can access the app (up to 5 concurrent users)
        Returns: (can_access: bool, message: str, user_count: int)
        """
        current_session_id = self.get_session_id()
        active_sessions = self.load_sessions()
        current_time = time.time()
        
        # Check if current user already has a session
        if current_session_id in active_sessions:
            # Update activity time
            active_sessions[current_session_id]['last_activity'] = current_time
            self.save_sessions(active_sessions)
            
            time_remaining = int(self.session_timeout - (current_time - active_sessions[current_session_id]['start_time']))
            user_count = len(active_sessions)
            return True, f"Session active. Time remaining: {time_remaining//60}m {time_remaining%60}s | Users online: {user_count}/5", user_count
        
        # Check if we can add a new user
        if len(active_sessions) < self.max_users:
            # Add new session
            active_sessions[current_session_id] = {
                'start_time': current_time,
                'last_activity': current_time,
                'user_agent': st.context.headers.get('user-agent', 'unknown')[:50] if hasattr(st, 'context') else 'unknown'
            }
            self.save_sessions(active_sessions)
            
            user_count = len(active_sessions)
            return True, f"Welcome! Session started | Users online: {user_count}/5", user_count
        
        # Maximum users reached
        else:
            user_count = len(active_sessions)
            # Find the session that will expire soonest
            min_remaining = min([self.session_timeout - (current_time - session['last_activity']) 
                               for session in active_sessions.values()])
            min_remaining = max(0, int(min_remaining))
            
            return False, f"Maximum 5 users reached. Next available in: {min_remaining//60}m {min_remaining%60}s", user_count
    
    def force_end_session(self, session_id=None):
        """Force end current or specific session"""
        active_sessions = self.load_sessions()
        
        if session_id:
            # End specific session
            if session_id in active_sessions:
                del active_sessions[session_id]
                self.save_sessions(active_sessions)
                return f"Session {session_id[:8]} ended!"
        else:
            # End current user's session
            current_session_id = self.get_session_id()
            if current_session_id in active_sessions:
                del active_sessions[current_session_id]
                self.save_sessions(active_sessions)
                return "Your session ended!"
        
        return "No session to end"
    
    def get_all_sessions_info(self):
        """Get info about all active sessions (for admin)"""
        active_sessions = self.load_sessions()
        sessions_info = []
        current_time = time.time()
        
        for session_id, session_data in active_sessions.items():
            time_remaining = int(self.session_timeout - (current_time - session_data['last_activity']))
            sessions_info.append({
                'id': session_id[:8],
                'user_agent': session_data.get('user_agent', 'unknown'),
                'time_remaining': f"{time_remaining//60}m {time_remaining%60}s",
                'active_for': f"{int((current_time - session_data['start_time'])//60)}m"
            })
        
        return sessions_info

# Helper functions for Streamlit
def init_session_manager():
    """Initialize session manager in Streamlit"""
    if 'session_manager' not in st.session_state:
        st.session_state.session_manager = SessionManager(session_timeout_minutes=5, max_concurrent_users=5)
    return st.session_state.session_manager

def check_session_middleware():
    """
    Middleware to check session before allowing app access
    Call this at the very beginning of your Streamlit app
    """
    session_manager = init_session_manager()
    can_access, message, time_remaining = session_manager.check_session_access()
    
    if not can_access:
        st.error("🚫 Access Denied")
        st.warning(message)
        
        # Show waiting screen
        st.markdown(f"""
        <div style="text-align: center; padding: 50px;">
            <h3>Please wait...</h3>
            <p>Another user is currently using the application.</p>
            <p><strong>Estimated wait time: {time_remaining//60} minutes {time_remaining%60} seconds</strong></p>
            <p>The page will auto-refresh in 30 seconds.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Auto-refresh every 30 seconds
        time.sleep(30)
        st.rerun()
        return False
    
    else:
        # Show session info in sidebar
        with st.sidebar:
            st.success("🟢 Session Active")
            st.info(message)
            
            # Add manual session end button
            if st.button("🔴 End My Session", help="End your session to allow others"):
                session_manager.force_end_session()
                st.success("Session ended!")
                st.rerun()
        
        return True

# Usage example for your main app
def main_app_with_session_control():
    """
    Your main app wrapped with session control
    """
    # FIRST: Check session access
    if not check_session_middleware():
        return  # Stop here if access denied
    
    # YOUR EXISTING APP CODE GOES HERE
    st.title("🏠 Gemma Family Assistant")
    # ... rest of your app code