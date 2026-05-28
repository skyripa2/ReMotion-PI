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
    <div class="hero-sub">Modelação e Controlo de um Exoesqueleto Robótico de Membro Superior</div>
    <div class="hero-desc">
        Desenvolvimento de uma solução robótica assistiva para o cotovelo focada na reabilitação ativa pós-AVC. 
        O sistema integra controlo mioelétrico proporcional submáximo, estratégias adaptativas <i>Assist-As-Needed</i> 
        e um modelo dinâmico de fadiga muscular simulado em ambiente virtual integrado.
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
        <div class="stat-label">Amplitude de flexão fisiológica do cotovelo visada pelo algoritmo de controlo do protótipo</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── ARQUITETURA DO SISTEMA (Malha de Controlo) ────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-title">🔄 Arquitetura do Sistema e Controlo em Malha Fechada</div>
    <p>O ReMotion opera sob uma malha de controlo fechada que une a intenção biológica do paciente à resposta mecânica do atuador virtual:</p>
    <div class="arch-grid">
        <div class="arch-card">
            <div class="arch-step">Passo 1</div>
            <h5>Atividade Muscular</h5>
            <p>O bíceps gera um sinal elétrico proporcional à intenção de flexão mecânica.</p>
        </div>
        <div class="arch-card">
            <div class="arch-step">Passo 2</div>
            <h5>Aquisição sEMG</h5>
            <p>Filtragem, retificação e cálculo do envelope de sinal (RMS) normalizado por subMVC.</p>
        </div>
        <div class="arch-card">
            <div class="arch-step">Passo 3</div>
            <h5>Algoritmo (MATLAB)</h5>
            <p>Processamento do torque humano real, avaliação do erro de rampa e cálculo da fadiga.</p>
        </div>
        <div class="arch-card">
            <div class="arch-step">Passo 4</div>
            <h5>Atuação (MuJoCo)</h5>
            <p>Injeção do torque de impedância corrigido no motor virtual do braço robótico.</p>
        </div>
        <div class="arch-card">
            <div class="arch-step">Passo 5</div>
            <h5>Feedback Cinemático</h5>
            <p>Os sensores angulares atualizam o erro de trajetória, reiniciando o loop de controlo.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── O PROJETO + IMAGEM CAD ───────────────────────────────────────────────────
col_t, col_i = st.columns([1.3, 1], gap="large")
with col_t:
    st.markdown("""
    <div class="section">
        <div class="section-title">🦾 Desenvolvimento e Engenharia do Protótipo</div>
        <p>O projeto aborda a modelação mecânica e o controlo dinâmico de uma ortótese ativa para o cotovelo. Utilizando dados de sEMG importados e processados via <strong>MATLAB</strong>, o sistema comanda o modelo físico construído e simulado no ecossistema de física <strong>MuJoCo</strong>.</p>
        <p>Diferente dos sistemas robóticos puramente passivos ou de trajetória rígida, o ReMotion foca-se na <strong>reabilitação orientada à tarefa e baseada no desafio</strong>. Através de leis de controlo adaptativas, o robô atua como um parceiro elástico: monitoriza as limitações do utilizador e fornece o binário estritamente necessário para que a trajetória fisiológica seja cumprida com sucesso.</p>
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

# ── OS TRÊS PILARES CIENTÍFICOS (Tecnologia) ──────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-title">⚙️ Estratégias de Modelação e Controlo</div>
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">📡</div>
            <h4>Controlo Proporcional por sEMG (subMVC)</h4>
            <p>O torque ativo gerado pelo utilizador é estimado diretamente do processamento do sinal elétrico do bíceps. A calibração assenta numa Contração Voluntária Máxima Submáxima (subMVC). Isto permite que pacientes com elevado défice motor consigam comandar o atuador sem sofrer espasmos ou lesões por sobre-esforço.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤝</div>
            <h4>Algoritmo Assist-As-Needed (AAN)</h4>
            <p>Implementado através de uma lei de Controlo por Impedância Proporcional. O exoesqueleto simula uma mola virtual rígida ($K = 40$ Nm/rad) apenas se detetar que o braço do paciente falha ou fica para trás relativamente à trajetória teórica de rampa, mantendo-se complacente e transparente enquanto a força do utilizador for suficiente.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔋</div>
            <h4>Modelo Dinâmica de Fadiga Muscular</h4>
            <p>Baseado num modelo matemático diferencial de primeira ordem. Quando o torque exercido ultrapassa o limiar de esforço estável de 30 Nm, a fadiga acumula-se continuamente. Ao cruzar o limiar crítico de tolerância neuromuscular (definido entre 70%-80%), o robô altera dinamicamente os ganhos de impedância e assume a compensação motora total.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── ANÁLISE DE SOLUÇÕES (Estado da Arte) ──────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-title">🔍 Enquadramento no Estado da Arte</div>
    <p>Comparação das metodologias avaliadas no projeto face às abordagens atuais de reabilitação neuromuscular:</p>
    <table class="comp-table">
        <thead><tr><th>Paradigma de Controlo</th><th>Abordagem Mecânica / Sinais</th><th>Limitação Identificada na Literatura</th></tr></thead>
        <tbody>
            <tr><td><strong>Fisioterapia Convencional</strong></td><td>Cinesioterapia assistida manualmente pelo terapeuta.</td><td><span class="lim">Falta de repetibilidade exata e ausência de biofeedback digital quantitativo.</span></td></tr>
            <tr><td><strong>Estimulação Elétrica (FES)</strong></td><td>Injeção de trens de pulso elétricos para contração artificial.</td><td><span class="lim">Despoleta fadiga periférica precoce e ignora o esforço cortical voluntário.</span></td></tr>
            <tr><td><strong>Exoesqueletos EMG Baseados em MVC</strong></td><td>Controlo mioelétrico mapeado por força voluntária máxima.</td><td><span class="lim">Inviável para pacientes neurológicos debilitados; induz risco de lesão muscular.</span></td></tr>
            <tr><td><strong>Controlo de Trajetória Rígido</strong></td><td>O motor executa uma posição fixa (posição pura), forçando o braço.</td><td><span class="lim">Provoca o fenómeno de slacking (anulação do esforço ativo do paciente).</span></td></tr>
            <tr class="hl"><td>✦ Abordagem ReMotion</td><td>Mapeamento subMVC + Impedância Assist-As-Needed + Modelo de Fadiga.</td><td style="color:#4dffa0;">✓ Maximiza a neuroplasticidade, garante segurança mecânica e adapta-se ao cansaço biológico.</td></tr>
        </tbody>
    </table>
</div>
""", unsafe_allow_html=True)

# ── RESULTADOS DAS SIMULAÇÕES (MATLAB / MUJOCO) ───────────────────────────────
st.markdown('<div class="section"><div class="section-title">📊 Resultados e Validação Computacional</div></div>', unsafe_allow_html=True)

res_c1, res_c2 = st.columns(2, gap="large")

with res_c1:
    st.markdown("""
    <div style="background:rgba(10,35,65,0.5); padding:1.5rem; border-radius:16px; border:1px solid rgba(100,180,255,0.1); height:100%;">
        <h5 style="color:#7ecfff; font-family:'Sora',sans-serif; margin-top:0;">Scenario A: Paciente Saudável / Controlo Ativo</h5>
        <p style="font-size:0.9rem; margin-bottom:0.5rem;">Nos ensaios onde o torque humano simulado acompanha estritamente os perfis de ativação, o erro cinemático mantém-se residual.</p>
        <ul style="font-size:0.85rem; color:#a0c0e0; padding-left:1.2rem;">
            <li>O exoesqueleto opera em modo de transparência cinemática (binário mínimo).</li>
            <li>O utilizador comanda de forma soberana a flexão até aos 135°.</li>
            <li>O modelo dinâmico regista estabilidade metabólica (sem acumulação de fadiga).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with res_c2:
    st.markdown("""
    <div style="background:rgba(10,35,65,0.5); padding:1.5rem; border-radius:16px; border:1px solid rgba(100,180,255,0.1); height:100%;">
        <h5 style="color:#ff9a9a; font-family:'Sora',sans-serif; margin-top:0;">Scenario B: Paciente Debilitado com Fadiga</h5>
        <p style="font-size:0.9rem; margin-bottom:0.5rem;">Simulação de fadiga muscular severa ou incapacidade motora abrupta a meio do exercício:</p>
        <ul style="font-size:0.85rem; color:#a0c0e0; padding-left:1.2rem;">
            <li>O desvio angular despoleta o crescimento imediato do erro de rampa.</li>
            <li>Ao cruzar o limiar de segurança, a rigidez do controlador ($K$) eleva-se para 40 Nm/rad.</li>
            <li>O atuador do exoesqueleto assume o torque em falta, corrigindo a trajetória e guiando o braço em segurança.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── EQUIPA CIENTÍFICA (PI) ───────────────────────────────────────────────────
st.markdown('<div class="section"><div class="section-title">👩‍🔬 Autores do Projeto</div><p>Equipa de projeto responsável pelo desenvolvimento do modelo matemático de controlo, simulação dinâmica e desenho mecânico do sistema ReMotion na unidade curricular de Projeto Integrador.</p></div>', unsafe_allow_html=True)

col_photo, col_names = st.columns([1.1, 1], gap="large")

with col_photo:
    if team_b64:
        st.markdown(f"""
        <div style="padding:1rem;background:rgba(13,61,110,0.3);border:1px solid rgba(100,180,255,0.12);border-radius:18px;text-align:center;">
            {team_tag}
            <p style="font-size:0.78rem;color:#5a8ab0;margin-top:0.8rem;margin-bottom:0;">A equipa ReMotion em Laboratório</p>
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
    <strong>ReMotion</strong> — Modelação e Controlo Adaptativo de Ortóteses Ativas.<br>
    Licenciatura em Engenharia Biomédica · Universidade do Minho<br>
    <strong>UC: Projeto Integrador em Engenharia Biomédica</strong><br><br>
    <span style="color:#5a8ab0; font-size:0.8rem; line-height:1.6; display:block; max-width:800px; margin:0 auto;">
        Corpo Docente de PI: Prof.ª Ana Vera Machado · Prof.ª Cristina Santos · Prof. José Gomes · Prof.ª Mariana Henriques · Prof. Victor Alves
    </span>
</div>
""", unsafe_allow_html=True)