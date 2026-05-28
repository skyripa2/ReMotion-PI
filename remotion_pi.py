import streamlit as st
import base64

st.set_page_config(
    page_title="ReMotion - Projeto Integrador",
    page_icon="🤖",
    layout="wide"
)

def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

# Mantém as tuas imagens de simulação/equipa se as tiveres na mesma pasta
exo_b64   = img_to_base64("exoesqueleto.png")
team_b64  = img_to_base64("team_photo.png")

exo_tag  = f'<img src="data:image/png;base64,{exo_b64}" style="width:100%;border-radius:14px;background:#e8edf2;"/>' if exo_b64 else ""
team_tag = f'<img src="data:image/png;base64,{team_b64}" style="width:100%;border-radius:14px;"/>' if team_b64 else ""

# ── ESTILOS CSS CUSTOMIZADOS ──────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family:'Inter',sans-serif; background:#05111c; color:#e8f0f8; }
.stApp { background:#05111c; }

/* HERO */
.hero {
    padding:5rem 3rem 4rem; border-radius:28px;
    background:linear-gradient(135deg,#0b2d4e 0%,#0d3d6e 50%,#0a4f8f 100%);
    text-align:center; margin-bottom:2.5rem;
    border:1px solid rgba(100,180,255,0.15);
}
.hero-tag {
    display:inline-block; background:rgba(30,120,255,0.2);
    border:1px solid rgba(100,180,255,0.3); color:#7ecfff;
    font-family:'Sora',sans-serif; font-size:0.75rem; font-weight:600;
    letter-spacing:0.15em; text-transform:uppercase;
    padding:0.35rem 1rem; border-radius:100px; margin-bottom:1.5rem;
}
.hero h1 { font-family:'Sora',sans-serif; font-size:4.5rem; font-weight:800; color:#fff; letter-spacing:-0.02em; margin:0 0 0.5rem; }
.hero h1 span { color:#4db8ff; }
.hero-sub  { font-family:'Sora',sans-serif; font-size:1.2rem; color:#a8d4ff; font-weight:300; }
.hero-desc { max-width:680px; margin:1.5rem auto 0; font-size:1rem; color:#c0d8f0; line-height:1.7; }

/* STATS */
.stats-bar { display:flex; gap:1.5rem; margin-bottom:2.5rem; }
.stat-card {
    flex:1; background:linear-gradient(135deg,rgba(13,61,110,0.6),rgba(10,40,80,0.8));
    border:1px solid rgba(100,180,255,0.12); border-radius:18px; padding:1.8rem 1.5rem; text-align:center;
}
.stat-number { font-family:'Sora',sans-serif; font-size:2.6rem; font-weight:800; color:#4db8ff; line-height:1; margin-bottom:0.5rem; }
.stat-label  { font-size:0.9rem; color:#a0c4e8; line-height:1.4; }
.stat-source { font-size:0.72rem; color:#5a8ab0; margin-top:0.4rem; }

/* SECTION WRAPPER */
.section {
    padding:2.5rem; border-radius:22px;
    background:rgba(13,40,70,0.4); border:1px solid rgba(100,180,255,0.08);
    margin-bottom:2rem;
}
.section-title { font-family:'Sora',sans-serif; font-size:1.6rem; font-weight:700; color:#7ecfff; margin-bottom:1.2rem; }
.section p { font-size:1rem; color:#c0d8f0; line-height:1.8; margin-bottom:1rem; }

/* ARCHITECTURE BLOCKS */
.arch-grid { display:flex; gap:1rem; margin-top:1rem; text-align:center; }
.arch-card {
    flex:1; background:rgba(15,55,95,0.4); border:1px solid rgba(100,180,255,0.1);
    border-radius:12px; padding:1.2rem; position:relative;
}
.arch-step { font-size:0.8rem; color:#4db8ff; font-weight:700; text-transform:uppercase; margin-bottom:0.4rem; }
.arch-card h5 { margin:0 0 0.4rem 0; font-family:'Sora',sans-serif; color:#fff; font-size:0.95rem; }
.arch-card p { font-size:0.8rem; color:#9abcdc; margin:0; line-height:1.4; }

/* FEATURE GRID */
.feature-grid { display:flex; gap:1.2rem; margin-top:1rem; }
.feature-card {
    flex:1; background:rgba(10,50,90,0.5); border:1px solid rgba(100,180,255,0.12);
    border-radius:16px; padding:1.6rem;
}
.feature-icon { font-size:1.8rem; margin-bottom:0.8rem; }
.feature-card h4 { font-family:'Sora',sans-serif; font-size:1.05rem; font-weight:700; color:#fff; margin-bottom:0.5rem; }
.feature-card p  { font-size:0.88rem; color:#a0c0e0; line-height:1.6; margin:0; }

/* COMPARISON TABLE */
.comp-table { width:100%; border-collapse:collapse; margin-top:1rem; font-size:0.9rem; }
.comp-table th { background:rgba(30,100,200,0.3); color:#7ecfff; font-family:'Sora',sans-serif; font-weight:600; padding:1rem 1.2rem; text-align:left; border-bottom:2px solid rgba(100,180,255,0.2); }
.comp-table td { padding:0.9rem 1.2rem; border-bottom:1px solid rgba(100,180,255,0.07); color:#c0d8f0; vertical-align:top; }
.comp-table tr:last-child td { border-bottom:none; }
.comp-table tr.hl td { background:rgba(30,100,200,0.12); color:#fff; }
.comp-table tr.hl td:first-child { color:#4db8ff; font-weight:700; }
.lim { display:inline-block; background:rgba(255,80,80,0.1); border:1px solid rgba(255,100,100,0.2); color:#ff9a9a; border-radius:6px; padding:0.2rem 0.5rem; font-size:0.82rem; }

/* FOOTER */
.footer { text-align:center; padding:3rem 2rem; border-top:1px solid rgba(100,180,255,0.08); margin-top:2rem; color:#4a7aaa; font-size:0.88rem; line-height:2; }
.footer strong { color:#6aaadd; }
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-tag">🔬 Projeto Integrador · Engenharia Biomédica · UMinho</div>
    <h1>Re<span>Motion</span></h1>
    <div class="hero-sub">Exoesqueleto Robótico com Controlo Eletromiográfico</div>
    <div class="hero-desc">
        Desenvolvimento de uma solução robótica assistiva para membros superiores focada na reabilitação pós-AVC. 
        O sistema integra controlo eletriomiográfico submáximo, estratégias adaptativas <i>Assist-As-Needed</i> 
        e um sistema dinâmico de fadiga muscular simulado em ambiente virtual integrado.
    </div>
</div>
""", unsafe_allow_html=True)

# ── STATS CLINICOS (Motivação do Projeto) ──────────────────────────────────────
st.markdown("""
<div class="stats-bar">
    <div class="stat-card">
        <div class="stat-number">15M</div>
        <div class="stat-label">Casos globais de AVC por ano, sendo a principal causa de incapacidade motora permanente</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">26/dia</div>
        <div class="stat-label">Média de novos episódios de AVC sinalizados pelas equipas de emergência em Portugal</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">50%</div>
        <div class="stat-label">Dos sobreviventes sofrem de hemiparesia crónica, afetando severamente o membro superior</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">135°</div>
        <div class="stat-label">Amplitude de flexão fisiológica do braço</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── ARQUITETURA DO SISTEMA (2 LINHAS DE 4 PASSOS) ─────────────────────────────
st.markdown('<div class="section"><div class="section-title">🔄 Arquitetura do Sistema</div>', unsafe_allow_html=True)

# Primeira Linha (Passos 1 ao 4)
l1_c1, l1_c2, l1_c3, l1_c4 = st.columns(4, gap="medium")
with l1_c1:
    st.markdown("""<div class="arch-card"><div class="arch-step">Passo 1</div><h5>Aquisição e Limpeza</h5><p>Leitura inicial dos dados dos canais EMG dos músculos (RBB, RDA, RDM, RDP).</p></div>""", unsafe_allow_html=True)
with l1_c2:
    st.markdown("""<div class="arch-card"><div class="arch-step">Passo 2</div><h5>Filtragem</h5><p>Tratamento do sinal e remoção de ruídos para isolar a componente elétrica muscular real.</p></div>""", unsafe_allow_html=True)
with l1_c3:
    st.markdown("""<div class="arch-card"><div class="arch-step">Passo 3</div><h5>Calibração (subMVC)</h5><p>Calibração do exoesqueleto baseada em contrações inferiores ao esforço máximo voluntário.</p></div>""", unsafe_allow_html=True)
with l1_c4:
    st.markdown("""<div class="arch-card"><div class="arch-step">Passo 4</div><h5>Limites Físicos</h5><p>Configuração das barreiras mecânicas: Cotovelo Máx = 60 Nm | Ombro Máx = 70 Nm.</p></div>""", unsafe_allow_html=True)

st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

# Segunda Linha (Passos 5 ao 8)
l2_c1, l2_c2, l2_c3, l2_c4 = st.columns(4, gap="medium")
with l2_c1:
    st.markdown("""<div class="arch-card"><div class="arch-step">Passo 5</div><h5>Torque do Paciente</h5><p>Cálculo da percentagem de esforço contínuo para estimar o torque humano gerado.</p></div>""", unsafe_allow_html=True)
with l2_c2:
    st.markdown("""<div class="arch-card"><div class="arch-step">Passo 6</div><h5>Défice Biológico</h5><p>Determinação da assistência: Torque em Falta = Torque Desejado - Torque do Paciente.</p></div>""", unsafe_allow_html=True)
with l2_c3:
    st.markdown("""<div class="arch-card"><div class="arch-step">Passo 7</div><h5>Saturação</h5><p>Garantia de que os valores de apoio calculados não ultrapassam os limites de segurança.</p></div>""", unsafe_allow_html=True)
with l2_c4:
    st.markdown("""<div class="arch-card"><div class="arch-step">Passo 8</div><h5>Atuação e Suavização</h5><p>Envio e otimização do perfil de força para aplicação suave no motor do exoesqueleto.</p></div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── O PROJETO + IMAGEM CAD ───────────────────────────────────────────────────
col_t, col_i = st.columns([1.3, 1], gap="large")
with col_t:
    st.markdown("""
    <div class="section">
        <div class="section-title">🦾 Desenvolvimento e Engenharia do Protótipo</div>
        <p>O projeto aborda a modelação mecânica e o controlo dinâmico de um exoesqueleto para membros superiores. Utilizando dados de EMG importados e processados via <strong>MATLAB</strong>, o sistema comanda o modelo físico construído e simulado no <strong>MuJoCo</strong>.</p>
        <p>Diferente dos sistemas robóticos puramente passivos, o ReMotion foca-se na <strong>reabilitação assistida e eficaz</strong>. Através do controlo por impedância, o o exoesqueleto tem em conta a gravidade e peso dos componentes, e o erro de posição.</p>
    </div>
    """, unsafe_allow_html=True)
with col_i:
    # Mostra a modelação matemática/FreeCAD do robô
    if exo_b64:
        st.markdown(f"""
        <div style="padding:1.2rem;background:rgba(13,61,110,0.3);border:1px solid rgba(100,180,255,0.12);border-radius:22px;text-align:center;">
            {exo_tag}
            <p style="font-size:0.78rem;color:#5a8ab0;margin-top:0.8rem;margin-bottom:0;">Figura 1 — Modelação Virtual do Sistema Cinemático</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("💡 Coloque o ficheiro 'exoesqueleto.png' no diretório para visualizar o modelo cinemático 3D.")

st.markdown("<br>", unsafe_allow_html=True)

# ── SELECÇÃO DE MATERIAIS DO DISPOSITIVO (NOVA) ───────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-title">🛠️ Seleção de Materiais e Biocompatibilidade</div>
    <p>A escolha dos materiais do protótipo baseou-se no equilíbrio entre resistência estrutural mecânica, leveza e conforto anatómico para o paciente:</p>
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">⛓️</div>
            <h4>Estrutura Principal</h4>
            <p><strong>PA12 + Fibras de Carbono</strong></p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🛡️</div>
            <h4>Camada de Amortecimento</h4>
            <p><strong>Espuma EVA (Etileno Acetato de Vinila)</strong></p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🧪</div>
            <h4>Interface com a Pele</h4>
            <p><strong>Silicone Elastómero (PDMS)</strong></p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎗️</div>
            <h4>Camada de Ajuste</h4>
            <p><strong>Velcro de Alta Fixação</strong></p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── OS TRÊS PILARES CIENTÍFICOS (Tecnologia) ──────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-title">⚙️ Tecnologias utilizadas</div>
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">📡</div>
            <h4>Controlo através de EMG com subMVC</h4>
            <p>O torque gerado pelo paciente é estimado diretamente do processamento do sinal. A calibração é feita numa Contração Voluntária Máxima Submáxima (subMVC). Isto permite que pacientes com elevado défice motor consigam utilizar o exoesqueleto sem sofrer espasmos ou lesões por esforço em demasia.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤝</div>
            <h4>Algoritmo Assist-As-Needed (AAN)</h4>
            <p>Implementado através de Controlo por Impedância, o exoesqueleto simula uma mola virtual quando deteta que o braço do paciente falha ou fica para trás relativamente ao ângulo desejado, mantendo-se transparente enquanto a força do utilizador for suficiente.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔋</div>
            <h4>Sistema de Deteção de Fadiga</h4>
            <p>Quando o torque exercido ultrapassa o limite de esforço estável de 30 Nm, a fadiga acumula-se continuamente. Ao cruzar o limite de tolerância (75%), o exoesqueleto altera o torque humano que é considerado na equação de impedância e fornece mais força para o movimento</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── ANÁLISE DE SOLUÇÕES (Estado da Arte) ──────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-title">🔍 Estado da Arte</div>
    <p>Comparação das metodologias avaliadas no projeto face às abordagens atuais de reabilitação:</p>
    <table class="comp-table">
        <thead><tr><th>Método</th><th>Abordagem</th><th>Limitações</th></tr></thead>
        <tbody>
            <tr><td><strong>Fisioterapia Convencional</strong></td><td>Exercícios assistidos manualmente pelo fisioterapeuta.</td><td><span class="lim">Elevada repetibilidade e ausência de biofeedback.</span></td></tr>
            <tr><td><strong>Estimulação Elétrica (FES)</strong></td><td>Injeção de impulsos elétricos para contração muscular.</td><td><span class="lim">Gera fadiga precoce e ignora o esforço voluntário do paciente.</span></td></tr>
            <tr><td><strong>Exoesqueletos EMG baseados em MVC</strong></td><td>Controlo eletromiográfico calibrado por contração voluntária máxima.</td><td><span class="lim">Inviável para pacientes neurológicos debilitados pois induz risco de lesão muscular.</span></td></tr>
            <tr><td><strong>Controlo por Posição</strong></td><td>O motor executa uma posição fixa, forçando o braço.</td><td><span class="lim">Provoca um movimento pouco natural e excesso de dependência.</span></td></tr>
            <tr class="hl"><td>✦ ReMotion</td><td>Calibração com subMVC + Sistema Assist-As-Needed + Deteção de Fadiga.</td><td><span class="lim">Ausência de movimento sem sinal EMG e sem acesso direto à intenção pura do paciente</td></tr>
        </tbody>
    </table>
</div>
""", unsafe_allow_html=True)

# ── RESULTADOS DAS SIMULAÇÕES (MATLAB / MUJOCO) ───────────────────────────────
st.markdown('<div class="section"><div class="section-title">📊 Resultados e Validação</div></div>', unsafe_allow_html=True)

res_c1, res_c2 = st.columns(2, gap="large")

with res_c1:
    st.markdown("""
    <div style="background:rgba(10,35,65,0.5); padding:1.5rem; border-radius:16px; border:1px solid rgba(100,180,255,0.1); height:100%;">
        <h5 style="color:#7ecfff; font-family:'Sora',sans-serif; margin-top:0;">Paciente Saudável</h5>
        <p style="font-size:0.9rem; margin-bottom:0.5rem;">Nos ensaios onde o torque humano simulado acompanha o torque desejado para o movimento, o erro de posição mantém-se residual.</p>
        <ul style="font-size:0.85rem; color:#a0c0e0; padding-left:1.2rem;">
            <li>O exoesqueleto opera em modo de transparência (quase não atua).</li>
            <li>O utilizador consegue participar na flexão toda.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with res_c2:
    st.markdown("""
    <div style="background:rgba(10,35,65,0.5); padding:1.5rem; border-radius:16px; border:1px solid rgba(100,180,255,0.1); height:100%;">
        <h5 style="color:#ff9a9a; font-family:'Sora',sans-serif; margin-top:0;"> Paciente Debilitado </h5>
        <p style="font-size:0.9rem; margin-bottom:0.5rem;">Simulação de um sinal EMG debilitado:</p>
        <ul style="font-size:0.85rem; color:#a0c0e0; padding-left:1.2rem;">
            <li>O erro de posição gera um maior torque do motor.</li>
            <li>O motor do exoesqueleto assume o torque em falta, corrigindo a trajetória e guiando o braço em segurança.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── EQUIPA CIENTÍFICA (PI) ───────────────────────────────────────────────────
st.markdown('<div class="section"><div class="section-title">👩‍🔬 Autores do Projeto</div><p>Equipa de projeto responsável pelo desenvolvimento do modelo matemático de controlo, simulação dinâmica e desenho mecânico do sistema ReMotion no âmbito da unidade curricular "Projeto Integrador em Engenharia Biomédica".</p></div>', unsafe_allow_html=True)

col_photo, col_names = st.columns([1.1, 1], gap="large")

with col_photo:
    if team_b64:
        st.markdown(f"""
        <div style="padding:1rem;background:rgba(13,61,110,0.3);border:1px solid rgba(100,180,255,0.12);border-radius:18px;text-align:center;">
            {team_tag}
            <p style="font-size:0.78rem;color:#5a8ab0;margin-top:0.8rem;margin-bottom:0;">A equipa ReMotion</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("💡 Coloque o ficheiro 'team_photo.png' para mostrar a fotografia do vosso grupo de PI.")

with col_names:
    st.markdown('<div style="padding:0.5rem 0;">', unsafe_allow_html=True)
    members = [
        ("Vera Campos", "a107235"),
        ("Ana Carolina Guimarães", "a107196"),
        ("Matilde Campos", "a107190"),
        ("Andriana Smoliy", "a107188"),
    ]
    for name, num in members:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:1rem;padding:0.8rem 0;border-bottom:1px solid rgba(100,180,255,0.08);">
            <div style="min-width:38px;height:38px;background:linear-gradient(135deg,#0d47a1,#1976d2);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.9rem;">👩‍🔬</div>
            <div>
                <div style="font-family:'Sora',sans-serif;font-weight:700;color:#fff;font-size:0.95rem;">{name}</div>
                <div style="font-size:0.8rem;color:#5a8ab0;">{num} · Licenciatura em Engenharia Biomédica, UMinho</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── FOOTER CIENTÍFICO ─────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <strong>ReMotion</strong> — Mais que movimento, devolvemos independência.<br>
    Licenciatura em Engenharia Biomédica · Universidade do Minho<br>
    <strong>UC: Projeto Integrador em Engenharia Biomédica</strong><br><br>
    <span style="color:#5a8ab0; font-size:0.8rem; line-height:1.6; display:block; max-width:800px; margin:0 auto;">
        Corpo Docente de PI: Prof.ª Ana Vera Machado · Prof.ª Cristina Santos · Prof. José Gomes · Prof.ª Mariana Henriques · Prof. Victor Alves
    </span>
</div>
""", unsafe_allow_html=True)
