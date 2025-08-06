import streamlit as st
import base64
from PIL import Image
import io

# Optional for better styling
import plotly.express as px
import plotly.graph_objects as go
# At the very top of your file, add these imports
from session_manager import check_session_middleware

# Then find your existing code and wrap it like this:
def main():
    # 🔒 SESSION CHECK FIRST
    if not check_session_middleware():
        return  # Blocks access if another user is active
    
    # YOUR EXISTING CODE GOES HERE EXACTLY AS IT IS
    st.set_page_config(
        page_title="Gemma Family Assistant",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Page config (at the very top)
    st.set_page_config(
        page_title="Gemma Family Assistant",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Main tabs definition
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "📊 Problem & Solution",
        "🏗️ Architecture", 
        "👦 Ajay (Education)", 
        "👩 Sita (Ayurveda)", 
        "👧 Jaya (Mental Health)", 
        "👨 Surya (Agriculture)", 
        "👴 Rao (Vision)", 
        "🚨 Emergency"
    ])



    # Problem → Solution → Impact Tab
    with tab1:
        st.header("📊 Problem → Solution → Impact")
        st.markdown("### *Ajay's Family Story with Real-World Statistics*")
        # Family Story Introduction
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    color: white; 
                    padding: 2rem; 
                    border-radius: 20px; 
                    margin: 2rem 0;
                    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
                    text-align: center;
                    position: relative;">
            <div style="font-size: 1.5rem; margin-bottom: 1rem; font-weight: bold;">
                👨‍👩‍👧‍👦 Meet the Ajay Family
            </div>
            <p style="font-size: 1.1rem; line-height: 1.8; margin: 0; font-style: italic;">
                Ajay, an 8th grader from rural India, dreams of learning beyond his limited school resources but cannot afford a tutor, 
                while his mother, Sita, relies on traditional Ayurveda to keep the family healthy. His younger sister, Jaya, struggles 
                with depression and has no access to mental health support, and his father, Surya, works tirelessly in the rice fields, 
                battling frequent crop diseases that threaten their livelihood. Their grandfather, Rao, has lost his vision with age 
                and depends on others to describe the world around him, making everyday life a challenge.
            </p>
            <div style="margin-top: 1.5rem; font-size: 1rem; opacity: 0.9;">
                <strong>Their story represents millions of rural Indian families facing similar challenges.</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")  # Divider before the problem sections
        # Custom CSS for this tab
        st.markdown("""
        <style>
        .problem-card {
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
            box-shadow: 0 4px 15px rgba(238, 90, 36, 0.3);
        }
        .solution-card {
            background: linear-gradient(135deg, #4834d4, #686de0);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
            box-shadow: 0 4px 15px rgba(72, 52, 212, 0.3);
        }
        .impact-card {
            background: linear-gradient(135deg, #00d2d3, #54a0ff);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
            box-shadow: 0 4px 15px rgba(0, 210, 211, 0.3);
        }
        .stat-highlight {
            font-size: 1.8rem;
            font-weight: bold;
            background: rgba(255,255,255,0.2);
            padding: 0.5rem 1rem;
            border-radius: 25px;
            display: inline-block;
            margin: 0.5rem;
            border: 2px solid rgba(255,255,255,0.3);
        }
        .character-header {
            text-align: center;
            font-size: 2rem;
            margin: 2rem 0 1rem 0;
            padding: 1rem;
            background: linear-gradient(135deg, #2c3e50, #3498db);
            color: white;
            border-radius: 15px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        }
        .section-divider {
            height: 3px;
            background: linear-gradient(90deg, #ff6b6b, #4834d4, #00d2d3);
            border: none;
            border-radius: 2px;
            margin: 2rem 0;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # 1. Ajay - Education
        st.markdown('<div class="character-header">👦 <strong>Ajay – The Student Without a Tutor</strong></div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="problem-card">
                <h4>🚨 PROBLEM</h4>
                <p>In rural India, <span class="stat-highlight">32.5%</span> of Class VIII students cannot read a Class II-level text, and <span class="stat-highlight">1 in 5</span> rural children in grades 1-8 depend on costly private tuition — a barrier for poor families.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="solution-card">
                <h4>💡 SOLUTION</h4>
                <p>Gemma 3N-powered offline tutor fine-tuned on Ajay's syllabus, guiding him in all subjects step-by-step with personalized explanations.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="impact-card">
                <h4>🎯 IMPACT</h4>
                <p>Affordable, private learning support at home, bridging the education gap for children like Ajay across rural India.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
        
        # 2. Sita - Ayurveda
        st.markdown('<div class="character-header">👩 <strong>Sita – The Homemaker Seeking Natural Remedies</strong></div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="problem-card">
                <h4>🚨 PROBLEM</h4>
                <p>Up to <span class="stat-highlight">70%</span> of rural households rely on traditional medicine, but much of it is based on unverified sources, risking harm to family health.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="solution-card">
                <h4>💡 SOLUTION</h4>
                <p>Gemma 3N fine-tuned on verified Ayurvedic datasets, delivering accurate, safe remedies in local languages with proper dosages.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="impact-card">
                <h4>🎯 IMPACT</h4>
                <p>Immediate, reliable home health guidance without costly or delayed clinic visits, ensuring family safety.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
        
        # 3. Jaya - Mental Health
        st.markdown('<div class="character-header">👧 <strong>Jaya – The Young Girl with Depression</strong></div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="problem-card">
                <h4>🚨 PROBLEM</h4>
                <p>Depression affects <span class="stat-highlight">14.49%</span> of rural residents, almost double the urban rate, yet only <span class="stat-highlight">20%</span> of Indians with mental illness receive treatment.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="solution-card">
                <h4>💡 SOLUTION</h4>
                <p>Gemma 3N mental health companion trained on approved depression-care material, accessible offline for private, stigma-free support.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="impact-card">
                <h4>🎯 IMPACT</h4>
                <p>Early access to emotional support, reducing stigma and preventing condition escalation in vulnerable youth.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
        
        # 4. Surya - Agriculture
        st.markdown('<div class="character-header">👨 <strong>Surya – The Rice Farmer Fighting Crop Loss</strong></div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="problem-card">
                <h4>🚨 PROBLEM</h4>
                <p>Rice diseases like bacterial blight can destroy up to <span class="stat-highlight">60%</span> of yields, and pests/diseases account for <span class="stat-highlight">40%</span> of crop losses globally every year.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="solution-card">
                <h4>💡 SOLUTION</h4>
                <p>Gemma 3N fine-tuned on agricultural advisory data, identifying risks from farmer-described symptoms or photos with treatment recommendations.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="impact-card">
                <h4>🎯 IMPACT</h4>
                <p>Timely intervention to save crops, protecting income and food supply for farming families across India.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
        
        # 5. Rao - Vision
        st.markdown('<div class="character-header">👴 <strong>Rao – The Grandfather Who Has Lost His Sight</strong></div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="problem-card">
                <h4>🚨 PROBLEM</h4>
                <p><span class="stat-highlight">33.8%</span> of Indians aged 45+ have distance vision impairment or blindness; <span class="stat-highlight">76.3%</span> have near vision loss, and most cases are avoidable.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="solution-card">
                <h4>💡 SOLUTION</h4>
                <p>Gemma 3N multimodal model describing images Rao captures, from reading signs to identifying objects, with detailed audio descriptions.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="impact-card">
                <h4>🎯 IMPACT</h4>
                <p>Restores independence, helping Rao navigate daily life confidently and maintain dignity in his golden years.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
        
        # 6. Emergency - Disaster Management
        st.markdown('<div class="character-header">🚨 <strong>When Disaster Strikes – Floods in Their Village</strong></div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="problem-card">
                <h4>🚨 PROBLEM</h4>
                <p>Floods cause <span class="stat-highlight">75%</span> of extreme weather deaths in India, killing an average of <span class="stat-highlight">1,671</span> people annually and causing <span class="stat-highlight">₹25,000+ crore</span> in yearly losses.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="solution-card">
                <h4>💡 SOLUTION</h4>
                <p>Gemma 3N fine-tuned on disaster-management guides, providing offline survival instructions when networks fail during emergencies.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="impact-card">
                <h4>🎯 IMPACT</h4>
                <p>Life-saving local guidance during emergencies, reducing panic and risk when every second counts for survival.</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Overall Impact Summary
        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; 
                    padding: 2rem; 
                    border-radius: 20px; 
                    text-align: center;
                    margin: 2rem 0;
                    box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
            <h2>🌟 Collective Impact: One AI, Six Life-Changing Solutions</h2>
            <p style="font-size: 1.2rem; margin: 1rem 0;">
                <strong>Serving 500M+ rural Indians</strong> with personalized, offline-capable AI assistance<br>
                across education, healthcare, mental wellness, agriculture, accessibility, and emergency response.
            </p>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; margin-top: 2rem;">
                <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; margin: 0.5rem;">
                    <div style="font-size: 2rem; font-weight: bold;">500M+</div>
                    <div>Rural Indians Reached</div>
                </div>
                <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; margin: 0.5rem;">
                    <div style="font-size: 2rem; font-weight: bold;">6</div>
                    <div>Critical Life Domains</div>
                </div>
                <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; margin: 0.5rem;">
                    <div style="font-size: 2rem; font-weight: bold;">₹0</div>
                    <div>Cost to Families</div>
                </div>
                <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; margin: 0.5rem;">
                    <div style="font-size: 2rem; font-weight: bold;">24/7</div>
                    <div>Offline Availability</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Architecture Tab - Streamlit Implementation
    with tab2:
        st.header("🏗️ System Architecture")
        
        # Custom CSS for architecture flow
        st.markdown("""
        <style>
            .arch-container {
                background: white;
                border-radius: 20px;
                padding: 30px;
                margin: 20px 0;
            }
            
            .arch-metrics {
                display: flex;
                justify-content: space-around;
                background: linear-gradient(135deg, #ff6b6b, #ee5a24);
                color: white;
                padding: 20px;
                border-radius: 15px;
                margin: 30px 0;
                text-align: center;
            }
            
            .arch-metric {
                flex: 1;
            }
            
            .metric-number {
                font-size: 2rem;
                font-weight: bold;
                display: block;
            }
            
            .metric-label {
                font-size: 0.9rem;
                opacity: 0.9;
            }
            
            .flow-step {
                display: flex;
                align-items: center;
                background: linear-gradient(135deg, #f8f9fa, #e9ecef);
                border-radius: 15px;
                padding: 20px;
                margin: 15px 0;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                position: relative;
            }
            
            .flow-step:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            }
            
            .step-number {
                width: 50px;
                height: 50px;
                border-radius: 50%;
                background: linear-gradient(135deg, #4834d4, #686de0);
                color: white;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: bold;
                font-size: 1.2rem;
                margin-right: 20px;
                flex-shrink: 0;
            }
            
            .step-content {
                flex: 1;
            }
            
            .step-title {
                font-size: 1.3rem;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 10px;
            }
            
            .step-description {
                color: #555;
                line-height: 1.6;
                margin-bottom: 10px;
            }
            
            .tech-tags {
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
                margin-top: 10px;
            }
            
            .tech-tag {
                background: linear-gradient(135deg, #2ed573, #7bed9f);
                color: white;
                padding: 4px 12px;
                border-radius: 15px;
                font-size: 0.8rem;
                font-weight: 500;
            }
            
            .dataset-tags {
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
                margin-top: 10px;
            }
            
            .dataset-tag {
                background: linear-gradient(135deg, #00d2d3, #54a0ff);
                color: white;
                padding: 6px 12px;
                border-radius: 20px;
                font-size: 0.85rem;
                font-weight: 500;
            }
            
            .final-summary {
                text-align: center;
                margin-top: 30px;
                padding: 25px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border-radius: 15px;
            }
            
            .arrow-down {
                text-align: center;
                font-size: 1.5rem;
                color: #4834d4;
                margin: 10px 0;
            }
            
            @media (max-width: 768px) {
                .arch-metrics {
                    flex-direction: column;
                    gap: 15px;
                }
                
                .flow-step {
                    flex-direction: column;
                    text-align: center;
                }
                
                .step-number {
                    margin-right: 0;
                    margin-bottom: 15px;
                }
            }
        </style>
        """, unsafe_allow_html=True)
        
        # Key Metrics Section
        st.markdown("""
        <div class="arch-metrics">
            <div class="arch-metric">
                <span class="metric-number">2,630</span>
                <span class="metric-label">Q&A Pairs Generated</span>
            </div>
            <div class="arch-metric">
                <span class="metric-number">5</span>
                <span class="metric-label">Specialized Domains</span>
            </div>
            <div class="arch-metric">
                <span class="metric-number">6</span>
                <span class="metric-label">Family Members Served</span>
            </div>
            <div class="arch-metric">
                <span class="metric-number">500M+</span>
                <span class="metric-label">Potential Users</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Flow Steps
        st.markdown("""
        <div class="flow-step">
            <div class="step-number">1</div>
            <div class="step-content">
                <div class="step-title">🎯 Problem Identification</div>
                <div class="step-description">
                    Identified critical challenges faced by rural Indian families across education, healthcare, agriculture, mental health, accessibility, and disaster management.
                </div>
            </div>
        </div>
        
        <div class="arrow-down">⬇️</div>
        
        <div class="flow-step">
            <div class="step-number">2</div>
            <div class="step-content">
                <div class="step-title">📚 Dataset Collection</div>
                <div class="step-description">
                    Gathered authoritative datasets across 5 critical domains from government and verified sources:
                </div>
                <div class="dataset-tags">
                    <span class="dataset-tag">📖 Class 8 NCERT Science</span>
                    <span class="dataset-tag">🌿 Ayurvedic Remedies</span>
                    <span class="dataset-tag">🌾 Rice Disease Management</span>
                    <span class="dataset-tag">💙 Depression Support</span>
                    <span class="dataset-tag">🚨 Disaster Management</span>
                </div>
            </div>
        </div>
        
        <div class="arrow-down">⬇️</div>
        
        <div class="flow-step">
            <div class="step-number">3</div>
            <div class="step-content">
                <div class="step-title">🔧 Data Extraction & Structure</div>
                <div class="step-description">
                    Used PyMuPDF to extract and structure content from PDFs, converting unstructured documents into machine-readable format for training.
                </div>
                <div class="tech-tags">
                    <span class="tech-tag">PyMuPDF</span>
                    <span class="tech-tag">Python</span>
                    <span class="tech-tag">JSON Structure</span>
                    <span class="tech-tag">Text Processing</span>
                </div>
            </div>
        </div>
        
        <div class="arrow-down">⬇️</div>
        
        <div class="flow-step">
            <div class="step-number">4</div>
            <div class="step-content">
                <div class="step-title">🤖 Base Model Setup</div>
                <div class="step-description">
                    Deployed Gemma 3N 4B model locally using Ollama for efficient inference and Q&A generation with multimodal capabilities.
                </div>
                <div class="tech-tags">
                    <span class="tech-tag">Ollama</span>
                    <span class="tech-tag">Gemma 3N 4B</span>
                    <span class="tech-tag">Local Deployment</span>
                    <span class="tech-tag">Multimodal</span>
                </div>
            </div>
        </div>
        
        <div class="arrow-down">⬇️</div>
        
        <div class="flow-step">
            <div class="step-number">5</div>
            <div class="step-content">
                <div class="step-title">❓ Q&A Generation</div>
                <div class="step-description">
                    Generated 2,630 high-quality Q&A pairs from structured data across all domains using Ollama API and Python automation scripts.
                </div>
                <div class="tech-tags">
                    <span class="tech-tag">Ollama API</span>
                    <span class="tech-tag">Python Scripts</span>
                    <span class="tech-tag">Automated Pipeline</span>
                    <span class="tech-tag">Quality Control</span>
                </div>
            </div>
        </div>
        
        <div class="arrow-down">⬇️</div>
        
        <div class="flow-step">
            <div class="step-number">6</div>
            <div class="step-content">
                <div class="step-title">🎯 Model Fine-tuning</div>
                <div class="step-description">
                    Fine-tuned Gemma 3N 4B model on Kaggle using the 2,630 Q&A pairs with domain-specific optimization for rural Indian context.
                </div>
                <div class="tech-tags">
                    <span class="tech-tag">Kaggle GPU</span>
                    <span class="tech-tag">Unsloth</span>
                    <span class="tech-tag">LoRA Fine-tuning</span>
                    <span class="tech-tag">Domain Adaptation</span>
                </div>
            </div>
        </div>
        
        <div class="arrow-down">⬇️</div>
        
        <div class="flow-step">
            <div class="step-number">7</div>
            <div class="step-content">
                <div class="step-title">📦 Model Conversion & Download</div>
                <div class="step-description">
                    Converted fine-tuned model to GGUF format for efficient local deployment and downloaded for local inference optimization.
                </div>
                <div class="tech-tags">
                    <span class="tech-tag">GGUF Format</span>
                    <span class="tech-tag">Model Quantization</span>
                    <span class="tech-tag">Local Storage</span>
                    <span class="tech-tag">Optimization</span>
                </div>
            </div>
        </div>
        
        <div class="arrow-down">⬇️</div>
        
        <div class="flow-step">
            <div class="step-number">8</div>
            <div class="step-content">
                <div class="step-title">🚀 Local Deployment</div>
                <div class="step-description">
                    Deployed fine-tuned model into Ollama for fast, offline-capable inference serving the family assistant application.
                </div>
                <div class="tech-tags">
                    <span class="tech-tag">Ollama Server</span>
                    <span class="tech-tag">Local API</span>
                    <span class="tech-tag">Offline Capable</span>
                    <span class="tech-tag">Fast Inference</span>
                </div>
            </div>
        </div>
        
        <div class="arrow-down">⬇️</div>
        
        <div class="flow-step">
            <div class="step-number">9</div>
            <div class="step-content">
                <div class="step-title">🔍 RAG Implementation</div>
                <div class="step-description">
                    Built Retrieval-Augmented Generation system using FAISS for semantic search on structured data, creating searchable knowledge base.
                </div>
                <div class="tech-tags">
                    <span class="tech-tag">FAISS Index</span>
                    <span class="tech-tag">Vector Embeddings</span>
                    <span class="tech-tag">Semantic Search</span>
                    <span class="tech-tag">Local Storage</span>
                </div>
            </div>
        </div>
        
        <div class="arrow-down">⬇️</div>
        
        <div class="flow-step">
            <div class="step-number">10</div>
            <div class="step-content">
                <div class="step-title">💻 User Interface</div>
                <div class="step-description">
                    Built intuitive Streamlit application for end users (family members) with specialized interfaces for each domain and multimodal capabilities.
                </div>
                <div class="tech-tags">
                    <span class="tech-tag">Streamlit</span>
                    <span class="tech-tag">Multimodal UI</span>
                    <span class="tech-tag">Family-Centric Design</span>
                    <span class="tech-tag">Responsive Layout</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Final Summary
        st.markdown("""
        <div class="final-summary">
            <h3>🎯 End Result: Complete AI-Powered Family Assistant</h3>
            <p style="font-size: 1.1rem; margin: 15px 0;">
                Offline-capable, domain-specific AI assistant serving 6 family members across 5 critical life domains 
                with 2,630 trained Q&A pairs and multimodal support for rural Indian communities.
            </p>
            <div style="display: flex; justify-content: space-around; margin-top: 20px; flex-wrap: wrap;">
                <div style="margin: 5px;">✅ Offline Capable</div>
                <div style="margin: 5px;">✅ Multimodal Support</div>
                <div style="margin: 5px;">✅ Domain Specialized</div>
                <div style="margin: 5px;">✅ Family Friendly</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        

    with tab3:
        # Sample questions for easy demo
        with st.expander("💡 Try These Sample Questions", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**📚 General Study Questions:**")
                st.write("• *What is irrigation and why do we need it?*")
                st.write("• *How should I prepare soil for growing crops?*")
                st.write("• *What are the steps for crop production?*")
                st.write("• *Difference between manure and fertilizers?*")
            
            with col2:
                st.markdown("**📄 Textbook Page Questions:**") 
                st.write("• *In page 15, what are agricultural practices?*")
                st.write("• *On page 16, what tools help prepare soil?*")
                st.write("• *From page 18, how do we sow seeds properly?*")
                st.write("• *Page 20 talks about manure - explain it*")
                # Header with Ajay's story
            st.header("👦 Ajay - Education Assistant")
        
        # Brief story context
        with st.container():
            st.markdown("""
            <div style="background-color: #f0f8ff; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <strong>Meet Ajay:</strong> An 8th grader from rural India who dreams of learning beyond his limited school resources. 
            Help him with his studies! 📚
            </div>
            """, unsafe_allow_html=True)
        
        # Initialize the education system
        @st.cache_resource
        def load_education_system():
            from education_qa import EducationQASystem
            return EducationQASystem("../datasets/education")
        
        try:
            qa_system = load_education_system()
            
            # Initialize chat messages in session state
            if "ajay_messages" not in st.session_state:
                st.session_state.ajay_messages = [
                    {"role": "assistant", "content": "Hi! I'm here to help you with your studies. You can ask me general questions about farming and agriculture, or ask about specific pages from your textbook!", "type": "intro"}
                ]
            
            # Display chat messages
            for message in st.session_state.ajay_messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
                    
                    # Show images if any
                    if "images" in message and message["images"]:
                        cols = st.columns(min(3, len(message["images"])))
                        for idx, img_data in enumerate(message["images"]):
                            with cols[idx % 3]:
                                image = qa_system.load_image_for_display(img_data['image_path'])
                                if image:
                                    st.image(image, caption=f"Figure {idx+1}", use_column_width=True)
                                    with st.expander(f"What this shows"):
                                        st.write(img_data['explanation'])
            
            # Chat input
            if prompt := st.chat_input("Ask me anything about farming, crops, or your textbook..."):
                
                # Add user message to chat history
                st.session_state.ajay_messages.append({"role": "user", "content": prompt})
                
                # Display user message
                with st.chat_message("user"):
                    st.write(prompt)
                
                # Generate and display assistant response
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        
                        # Process the question
                        result = qa_system.process_question(prompt)
                        
                        # Display the answer
                        st.write(result['answer'])
                        
                        # Display images if any
                        images_to_store = []
                        if result.get('images') and len(result['images']) > 0:
                            st.write("**📸 Related Images:**")
                            
                            cols = st.columns(min(3, len(result['images'])))
                            for idx, img_data in enumerate(result['images']):
                                with cols[idx % 3]:
                                    image = qa_system.load_image_for_display(img_data['image_path'])
                                    if image:
                                        st.image(image, caption=f"Figure {idx+1}", use_column_width=True)
                                        with st.expander(f"What this shows"):
                                            st.write(img_data['explanation'])
                                        
                                        images_to_store.append(img_data)
                        
                        # Show question type info
                        if result['type'] == 'page_based':
                            st.info(f"📖 Information from page {result.get('page_number')}")
                        else:
                            st.info("🔍 Answer from multiple sources")
                
                # Add assistant response to chat history
                assistant_message = {
                    "role": "assistant", 
                    "content": result['answer'],
                    "type": result['type']
                }
                
                if images_to_store:
                    assistant_message["images"] = images_to_store
                
                st.session_state.ajay_messages.append(assistant_message)
            
            # Clear chat button (in sidebar or bottom)
            # if len(st.session_state.ajay_messages) > 1:  # More than just the intro message
            #     with st.sidebar:
            #         st.write("---")
            #         if st.button("🗑️ Clear Chat", help="Start a new conversation"):
            #             st.session_state.ajay_messages = [
            #                 {"role": "assistant", "content": "Hi! I'm here to help you with your studies. You can ask me general questions about farming and agriculture, or ask about specific pages from your textbook!", "type": "intro"}
            #             ]
            #             st.rerun()
            
            # # Sample questions in sidebar
            # with st.sidebar:
            #     st.write("---")
            #     st.subheader("💡 Try These Questions")
                
            #     st.write("**General Questions:**")
            #     if st.button("What is irrigation?", key="sample1"):
            #         st.session_state.next_question = "What is irrigation and why is it important?"
            #         st.rerun()
                
            #     if st.button("Steps for crop production?", key="sample2"):
            #         st.session_state.next_question = "What are the basic steps for crop production?"
            #         st.rerun()
                
            #     st.write("**Page Questions:**")
            #     if st.button("About page 15", key="sample3"):
            #         st.session_state.next_question = "In page 15, explain about agricultural practices"
            #         st.rerun()
                
            #     if st.button("About page 20", key="sample4"):
            #         st.session_state.next_question = "Page 20 talks about manure - explain it"
            #         st.rerun()
            
            # Handle sample question clicks
            if "next_question" in st.session_state:
                # Add the question to chat and process it
                question = st.session_state.next_question
                del st.session_state.next_question
                
                # Add user message
                st.session_state.ajay_messages.append({"role": "user", "content": question})
                
                # Process and add response
                result = qa_system.process_question(question)
                assistant_message = {
                    "role": "assistant", 
                    "content": result['answer'],
                    "type": result['type']
                }
                
                if result.get('images'):
                    assistant_message["images"] = result['images']
                
                st.session_state.ajay_messages.append(assistant_message)
                st.rerun()
        
        except Exception as e:
            st.error("❌ Ajay's study helper isn't available right now")
            st.write("Please check that all files are properly set up.")
            
            with st.expander("Technical Details"):
                st.code(str(e))

    # Status in sidebar
    def show_ajay_status():
        """Show system status in sidebar"""
        with st.sidebar:
            st.subheader("👦 Ajay's Helper")
            
            try:
                from education_qa import EducationQASystem
                qa_system = EducationQASystem("../datasets/education")
                
                textbook_ready = len(qa_system.structured_data) > 0
                ai_ready = (qa_system.rag_index_path / "faiss_index.bin").exists()
                
                if textbook_ready and ai_ready:
                    st.success("✅ Ready to help!")
                    st.write(f"📚 Sections: {len(qa_system.structured_data)}")
                else:
                    st.warning("⚠️ Setting up...")
                    
            except Exception:
                st.error("❌ Helper offline")

    # Add this call in your main app
    # show_ajay_status()


    # Tab 4: Sita (Ayurveda) - Chatbot style like tab3

    with tab4:
        # Sample questions for easy demo
        with st.expander("💡 Try These Sample Questions", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**🌿 Common Health Issues:**")
                st.write("• *How long should I continue giving the onion decoction to my child with a cold or cough?*")
                st.write("• *I'm worried about my child's fever.  What Ayurvedic approach involving Tulsi can I take?*")
                st.write("• *My child has lost his appetite.  Is there a natural, Ayurvedic way to encourage him to eat using Neem?*")
                st.write("• *My child has lost his appetite.  Is there a natural, Ayurvedic way to encourage him to eat using Neem?*")
            
            with col2:
                st.markdown("**🍯 Preventive Care:**") 
                st.write("• *Is it okay to give onion to infants?*")
                st.write("• *Is it safe to give Pippali to children? Are there any dosage considerations for kids?*")
                st.write("• *My daughter has been struggling with diarrhea.  Is Saunf a safe and effective Ayurvedic remedy for this, and how should I administer it?*")
                st.write("• *Is there a specific time of day that's best to consume Methi for its health benefits in Ayurveda?*")

        # Header with Sita's story
        st.header("👩 Sita - Ayurvedic Home Remedies")

        # Brief story context
        with st.container():
            st.markdown("""
            <div style="background-color: #f0fff0; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <strong>Meet Sita:</strong> A caring homemaker who believes in traditional Ayurvedic remedies 
            to keep her family healthy. She prefers natural treatments over medicines! 🌿
            </div>
            """, unsafe_allow_html=True)

        # Initialize the ayurveda system
        @st.cache_resource
        def load_ayurveda_system():
            from ayurveda_qa import AyurvedaQASystem
            return AyurvedaQASystem("datasets/ayurveda")

        try:
            qa_system = load_ayurveda_system()
            
            # Initialize chat messages in session state
            if "sita_messages" not in st.session_state:
                st.session_state.sita_messages = [
                    {"role": "assistant", "content": "Namaste! I'm here to help you with traditional Ayurvedic remedies for your family's health. Ask me about any health concerns!", "type": "intro"}
                ]
            
            # Display chat messages
            for message in st.session_state.sita_messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
            
            # Chat input
            if prompt := st.chat_input("Ask me about natural remedies for your family..."):
                
                # Add user message to chat history
                st.session_state.sita_messages.append({"role": "user", "content": prompt})
                
                # Display user message
                with st.chat_message("user"):
                    st.write(prompt)
                
                # Generate and display assistant response
                with st.chat_message("assistant"):
                    with st.spinner("Consulting Ayurvedic wisdom..."):
                        
                        # Process the question using ayurveda system
                        answer = qa_system.ask_remedy(prompt)
                        
                        # Display the answer
                        st.write(answer)
                        
                        # Show remedy type info
                        st.info("🌿 Traditional Ayurvedic remedy")
                
                # Add assistant response to chat history
                assistant_message = {
                    "role": "assistant", 
                    "content": answer,
                    "type": "remedy"
                }
                
                st.session_state.sita_messages.append(assistant_message)
            

        
        except Exception as e:
            st.error("❌ Sita's remedy helper isn't available right now")
            st.write("Please check that ayurveda_qa.py and datasets are properly set up.")
            
            with st.expander("Technical Details"):
                st.code(str(e))

    # Tab 5: Jaya (Mental Health) - Chatbot for depression support

    with tab5:
        # Sample questions for easy demo
        with st.expander("💡 Try These Sample Questions", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**💙 Understanding Depression:**")
                st.write("• *I've been feeling sad and empty lately. Could this be depression?*")
                st.write("• *What are the main symptoms of depression I should know about?*")
                st.write("• *How is depression different from just feeling down sometimes?*")
                st.write("• *What causes depression and why does it happen?*")
            
            with col2:
                st.markdown("**🤝 Getting Help & Support:**") 
                st.write("• *What treatment options are available for depression?*")
                st.write("• *How can I support a friend who seems depressed?*")
                st.write("• *Where can I find help if I think I'm depressed?*")
                st.write("• *How do I know if someone needs immediate help?*")

        # Header with Jaya's story
        st.header("👧 Jaya - Mental Health Support")

        # Brief story context
        with st.container():
            st.markdown("""
            <div style="background-color: #f0f8ff; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <strong>Meet Jaya:</strong> Ajay's younger sister who struggles with depression and has no access 
            to mental health support. She needs understanding, guidance, and hope. 💙
            </div>
            """, unsafe_allow_html=True)

        # Initialize the mental health system
        @st.cache_resource
        def load_mental_health_system():
            from mental_health_qa import MentalHealthQASystem
            return MentalHealthQASystem("datasets/depression")

        try:
            qa_system = load_mental_health_system()
            
            # Initialize chat messages in session state
            if "jaya_messages" not in st.session_state:
                st.session_state.jaya_messages = [
                    {"role": "assistant", "content": "Hi there! I'm here to provide support and information about mental health. You can ask me anything about depression, getting help, or supporting others. Remember, you're not alone! 💙", "type": "intro"}
                ]
            
            # Display chat messages
            for message in st.session_state.jaya_messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
            
            # Chat input
            if prompt := st.chat_input("Ask me about mental health, depression, or getting support..."):
                
                # Add user message to chat history
                st.session_state.jaya_messages.append({"role": "user", "content": prompt})
                
                # Display user message
                with st.chat_message("user"):
                    st.write(prompt)
                
                # Generate and display assistant response
                with st.chat_message("assistant"):
                    with st.spinner("Thinking with care..."):
                        
                        # Process the question using mental health system
                        answer = qa_system.get_support(prompt)
                        
                        # Display the answer
                        st.write(answer)
                        
                        # Show supportive info
                        st.info("💙 Remember: This is general information. For immediate help, please contact a mental health professional or crisis hotline.")
                
                # Add assistant response to chat history
                assistant_message = {
                    "role": "assistant", 
                    "content": answer,
                    "type": "support"
                }
                
                st.session_state.jaya_messages.append(assistant_message)
        
        except Exception as e:
            st.error("❌ Jaya's mental health helper isn't available right now")
            st.write("Please check that mental_health_qa.py and datasets are properly set up.")
            
            with st.expander("Technical Details"):
                st.code(str(e))

        # Important resources and disclaimer
        with st.container():
            st.markdown("---")
            st.markdown("""
            <div style="background-color: #fff3cd; padding: 15px; border-radius: 10px; border-left: 4px solid #ffc107;">
            <strong>🚨 Crisis Resources:</strong><br>
            • <strong>Emergency:</strong> Call 108 (India) or your local emergency number<br>
            • <strong>Suicide Prevention:</strong> Call 9152987821 (AASRA India)<br>
            • <strong>Mental Health Helpline:</strong> Call 9820466726<br><br>
            <em>If you or someone you know is in immediate danger, please seek professional help immediately.</em>
            </div>
            """, unsafe_allow_html=True)

    # Tab 8: Emergency Management - Chatbot for disaster preparedness

    # Tab 8: Emergency Management - Simple chatbot

    with tab8:
        st.header("🚨 Emergency Management")

        with st.expander("💡 Try These Sample Questions", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**🌪️ Natural Disasters:**")
                st.write("• *What should I do during a cyclone warning?*")
                st.write("• *How to prepare for earthquakes in India?*")
                st.write("• *What are the safety measures during floods?*")
                st.write("• *How to protect myself during a heatwave?*")
            
            with col2:
                st.markdown("**🚨 Emergency Response:**") 
                st.write("• *What is the emergency number in India?*")
                st.write("• *How to identify signs of a landslide?*")
                st.write("• *What to do after a tsunami warning?*")
                st.write("• *How to prepare an emergency kit for disasters?*")

        
        # Initialize the emergency system
        @st.cache_resource
        def load_emergency_system():
            from emergency_qa import EmergencyQASystem
            return EmergencyQASystem()

        try:
            qa_system = load_emergency_system()
            
            # Initialize chat messages
            if "emergency_messages" not in st.session_state:
                st.session_state.emergency_messages = [
                    {"role": "assistant", "content": "🚨 Emergency Assistant Ready! I can help with disaster preparedness and safety."}
                ]
            
            # Display chat messages
            for message in st.session_state.emergency_messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
            
            # Chat input
            if prompt := st.chat_input("Ask about disasters, emergencies, or safety..."):
                
                # Add user message
                st.session_state.emergency_messages.append({"role": "user", "content": prompt})
                
                # Display user message
                with st.chat_message("user"):
                    st.write(prompt)
                
                # Generate response
                with st.chat_message("assistant"):
                    with st.spinner("Getting emergency guidance..."):
                        answer = qa_system.get_emergency_guidance(prompt)
                        st.write(answer)
                
                # Add assistant response
                st.session_state.emergency_messages.append({"role": "assistant", "content": answer})
        
        except Exception as e:
            st.error(f"❌ Emergency system error: {e}")
            st.info("📞 For immediate emergencies, call 112")

    # Tab 7: Rao (Vision) - Vision Assistant
    # Tab 7: Rao (Vision) - Vision Assistant with Voice Input
    # Tab 7: Rao (Vision) - Vision Assistant with Voice Input
    with tab7:
        st.header("👴 Rao - Vision Assistant")
        
        # Rao's story context
        with st.container():
            st.markdown("""
            <div style="background-color: #f5f5f5; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <strong>Meet Rao:</strong> Ajay's grandfather who has lost his vision with age and depends on others 
            to describe the world around him. Help him see through AI! 👁️
            </div>
            """, unsafe_allow_html=True)
        
        # Initialize the vision system
        @st.cache_resource
        def load_vision_system():
            from rao_vision_qa import RaoVisionQASystem
            return RaoVisionQASystem()
        
        try:
            vision_system = load_vision_system()
            
            # Two columns layout
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.subheader("📸 Step 1: Upload Picture")
                uploaded_image = st.file_uploader(
                    "Choose an image...", 
                    type=['jpg', 'jpeg', 'png'],
                    help="Upload any image for Rao to understand"
                )
                
                if uploaded_image is not None:
                    st.image(uploaded_image, caption="Image for Rao", use_column_width=True)
            
            with col2:
                st.subheader("🎤 Step 2: Record Question")
                
                # Fixed st_audiorec usage
                try:
                    from st_audiorec import st_audiorec
                    
                    st.write("Click the microphone to record your question:")
                    audio_data = st_audiorec()  # Simple usage without parameters
                    
                    if audio_data is not None:
                        st.success("🎤 Audio recorded!")
                        
                except ImportError:
                    st.warning("Voice recording not available. Install: pip install streamlit-audiorec")
                    audio_data = None
                except Exception as e:
                    st.error(f"Audio recording error: {e}")
                    audio_data = None
            
            # Process section
            st.write("---")
            st.subheader("🔊 What Rao Hears:")
            
            if uploaded_image is not None:
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("👁️ Describe Image Only", type="secondary"):
                        with st.spinner("Looking at the image for Rao..."):
                            description = vision_system.simple_image_description(uploaded_image)
                            
                            # Display description
                            st.write(description)
                            
                            # Speak it out
                            with st.spinner("Speaking description..."):
                                if vision_system.speak_text(description):
                                    st.success("✅ Description spoken aloud!")
                                else:
                                    st.info("🔇 Text-to-speech not available")
                
                with col2:
                    if st.button("🎤👁️ Process Voice + Image", type="primary", disabled=(audio_data is None)):
                        if audio_data is not None:
                            with st.spinner("Understanding your question and looking at the image..."):
                                description = vision_system.process_with_audio_and_image(uploaded_image, audio_data)
                                
                                # Display description
                                st.write(description)
                                
                                # Speak it out
                                with st.spinner("Speaking answer..."):
                                    if vision_system.speak_text(description):
                                        st.success("✅ Answer spoken aloud!")
                                    else:
                                        st.info("🔇 Text-to-speech not available")
                        else:
                            st.warning("Please record an audio question first!")
            
            else:
                st.info("👆 Please upload an image to help Rao see what's around him")
            
            # Instructions and examples remain the same...
            st.write("---")
            st.markdown("""
            <div style="background-color: #e8f4fd; padding: 15px; border-radius: 10px;">
            <strong>📱 How this works for Rao:</strong><br>
            1. 📸 <strong>Upload a picture</strong> - Take photo with phone/camera<br>
            2. 🎤 <strong>Record your question</strong> - Click microphone and ask what you want to know<br>
            3. 🎯 <strong>Choose processing type:</strong><br>
            &nbsp;&nbsp;&nbsp;• <strong>Image Only</strong> - Get general description<br>
            &nbsp;&nbsp;&nbsp;• <strong>Voice + Image</strong> - Answer your specific question<br>
            4. 🔊 <strong>Listen</strong> - AI will speak the answer aloud<br><br>
            <em>Perfect for helping Rao understand his surroundings!</em>
            </div>
            """, unsafe_allow_html=True)
        
        except Exception as e:
            st.error("❌ Rao's vision helper isn't available right now")
            st.write("Please check that rao_vision_qa.py is properly set up.")
            
            with st.expander("Technical Details"):
                st.code(str(e))

    # Tab 6: Surya (Agriculture) - Add this to your main Streamlit app

    # Tab 6: Surya (Agriculture) - Add this to your main Streamlit app

    with tab6:
        # Sample questions for easy demo
        with st.expander("💡 Try These Sample Questions", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**🌾 Rice Farming Questions:**")
                st.write("• *When is the best time to apply chemical sprays for Brown Spot disease control in Indian rice fields?*")
                st.write("• *How can Indian rice farmers minimize the risk of Brown Spot disease infection at the seedling stage?*")
                st.write("• *What role does water management play in Brown Spot disease control?*")
                st.write("• *In rice farming in India, if the panicle neck turns black, weak, and droops, could it be neck blast (Pyricularia oryzae)? What should I do immediately?*")
            
            with col2:
                st.markdown("**🌱 General Farming:**") 
                st.write("• *As an Indian rice farmer, how can I confirm bacterial leaf blight infection during the growing season?*")
                st.write("• *What are the key visible signs of bacterial leaf blight in rice, and how do they change as the disease progresses?*")
                st.write("• *What preventive measures can Indian rice farmers take against sheath rot (Sarocladium oryzae) in transplanted crops?*")
                st.write("• *What fungal growth appears inside affected sheaths and young panicles due to Sarocladium oryzae?*")


        # Header with Surya's story
        st.header("👨 Surya - Rice Farming Assistant")
        
        # Brief story context
        with st.container():
            st.markdown("""
            <div style="background-color: #f0fff4; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <strong>Meet Surya:</strong> Ajay's father who works tirelessly in the rice fields, 
            battling frequent crop diseases that threaten their livelihood. Help him save his crops! 🌾
            </div>
            """, unsafe_allow_html=True)
        
        # Initialize the agriculture system
        @st.cache_resource
        def load_agriculture_system():
            from agriculture_qa import AgricultureQASystem
            return AgricultureQASystem("../datasets/rice_diseases")  # Updated path
        
        try:
            qa_system = load_agriculture_system()
            
            # Initialize chat messages in session state
            if "surya_messages" not in st.session_state:
                st.session_state.surya_messages = [
                    {"role": "assistant", "content": "Namaste! I'm here to help you with rice farming, crop diseases, and agricultural guidance. Ask me anything about farming!", "type": "intro"}
                ]
            
            # Display chat messages
            for message in st.session_state.surya_messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
                    
                    # Show images if any
                    if "images" in message and message["images"]:
                        cols = st.columns(min(3, len(message["images"])))
                        for idx, img_data in enumerate(message["images"]):
                            with cols[idx % 3]:
                                image = qa_system.load_image_for_display(img_data['image_path'])
                                if image:
                                    st.image(image, caption=f"Figure {idx+1}", use_column_width=True)
                                    with st.expander(f"What this shows"):
                                        st.write(img_data['explanation'])
            
            # Chat input
            if prompt := st.chat_input("Ask me about rice farming, crop diseases, or agricultural practices..."):
                
                # Add user message to chat history
                st.session_state.surya_messages.append({"role": "user", "content": prompt})
                
                # Display user message
                with st.chat_message("user"):
                    st.write(prompt)
                
                # Generate and display assistant response
                with st.chat_message("assistant"):
                    with st.spinner("Thinking about your farming question..."):
                        
                        # Process the farming question
                        result = qa_system.process_farming_question(prompt)
                        
                        # Display the answer
                        st.write(result['answer'])
                        
                        # Display images if any
                        images_to_store = []
                        if result.get('images') and len(result['images']) > 0:
                            st.write("**📸 Related Agricultural Images:**")
                            
                            cols = st.columns(min(3, len(result['images'])))
                            for idx, img_data in enumerate(result['images']):
                                with cols[idx % 3]:
                                    image = qa_system.load_image_for_display(img_data['image_path'])
                                    if image:
                                        st.image(image, caption=f"Figure {idx+1}", use_column_width=True)
                                        with st.expander(f"What this shows"):
                                            st.write(img_data['explanation'])
                                        
                                        images_to_store.append(img_data)
                        
                        # Show question type info
                        if result['type'] == 'full_pipeline':
                            st.info(f"🌾 Combined answer from: {result.get('sources', 'Fine-tuned model + Knowledge base')}")
                        elif result['type'] == 'gemma_family_only':
                            st.info("🤖 Answer from fine-tuned farming model only")
                        else:
                            st.info("🔍 Answer from farming assistant")
                
                # Add assistant response to chat history
                assistant_message = {
                    "role": "assistant", 
                    "content": result['answer'],
                    "type": result['type']
                }
                
                if images_to_store:
                    assistant_message["images"] = images_to_store
                
                st.session_state.surya_messages.append(assistant_message)
            
            # Clear chat button (in sidebar or bottom)
            # if len(st.session_state.surya_messages) > 1:  # More than just the intro message
            #     with st.sidebar:
            #         st.write("---")
            #         if st.button("🗑️ Clear Chat", help="Start a new conversation", key="clear_surya"):
            #             st.session_state.surya_messages = [
            #                 {"role": "assistant", "content": "Namaste! I'm here to help you with rice farming, crop diseases, and agricultural guidance. Ask me anything about farming!", "type": "intro"}
            #             ]
            #             st.rerun()
            
            # # Sample questions in sidebar
            # with st.sidebar:
            #     st.write("---")
            #     st.subheader("💡 Try These Questions")
                
            #     st.write("**🌾 Rice Questions:**")
            #     if st.button("About bacterial blight", key="agri_sample1"):
            #         st.session_state.next_agri_question = "What is bacterial blight in rice and how to treat it?"
            #         st.rerun()
                
            #     if st.button("Pest identification", key="agri_sample2"):
            #         st.session_state.next_agri_question = "How to identify pest damage in rice crops?"
            #         st.rerun()
                
            #     st.write("**🌱 General Farming:**")
            #     if st.button("Soil preparation", key="agri_sample3"):
            #         st.session_state.next_agri_question = "How to prepare soil for crop cultivation?"
            #         st.rerun()
                
            #     if st.button("Irrigation methods", key="agri_sample4"):
            #         st.session_state.next_agri_question = "What irrigation methods work best for rice?"
            #         st.rerun()
            
            # Handle sample question clicks
            if "next_agri_question" in st.session_state:
                # Add the question to chat and process it
                question = st.session_state.next_agri_question
                del st.session_state.next_agri_question
                
                # Add user message
                st.session_state.surya_messages.append({"role": "user", "content": question})
                
                # Process and add response
                result = qa_system.process_farming_question(question)
                assistant_message = {
                    "role": "assistant", 
                    "content": result['answer'],
                    "type": result['type']
                }
                
                if result.get('images'):
                    assistant_message["images"] = result['images']
                
                st.session_state.surya_messages.append(assistant_message)
                st.rerun()
        
        except Exception as e:
            st.error("❌ Surya's farming helper isn't available right now")
            st.write("Please check that agriculture_qa.py and datasets are properly set up.")
            
            with st.expander("Technical Details"):
                st.code(str(e))

    # Status in sidebar (add this function)
    def show_surya_status():
        """Show agriculture system status in sidebar"""
        with st.sidebar:
            st.subheader("👨 Surya's Helper")
            
            try:
                from agriculture_qa import AgricultureQASystem
                qa_system = AgricultureQASystem("../datasets/rice_diseases")  # Updated path
                
                data_ready = len(qa_system.structured_data) > 0
                rag_ready = qa_system.faiss_index is not None
                
                if data_ready and rag_ready:
                    st.success("✅ Ready to help!")
                    st.write(f"🌾 Knowledge: {len(qa_system.text_chunks)} chunks")
                elif data_ready:
                    st.warning("⚠️ RAG index missing")
                    st.write(f"📚 Sections: {len(qa_system.structured_data)}")
                else:
                    st.warning("⚠️ Setting up...")
                    
            except Exception:
                st.error("❌ Helper offline")

    # Add this call in your main app
    # show_surya_status()

# Add this at the very bottom
if __name__ == "__main__":
    main()    