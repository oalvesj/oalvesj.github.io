// Seleção de elementos do DOM
const themeToggleBtn = document.getElementById('theme-toggle-btn');
const menuToggleBtn = document.getElementById('menu-toggle-btn');
const body = document.body;

// Função para alternar entre modo claro e escuro
function toggleTheme() {
    // Verifica se o tema atual é escuro
    const isDarkMode = body.getAttribute('data-theme') === 'dark';
    
    // Alterna o tema
    if (isDarkMode) {
        body.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
    } else {
        body.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    }
}

// Função para alternar o menu mobile
function toggleMenu() {
    body.classList.toggle('mobile-menu-active');
}

// Inicialização do tema com base na preferência salva
function initTheme() {
    // Verifica se há uma preferência salva no localStorage
    const savedTheme = localStorage.getItem('theme');
    
    // Se houver uma preferência salva, aplica-a
    if (savedTheme === 'dark') {
        body.setAttribute('data-theme', 'dark');
    }
    
    // Verifica a preferência do sistema se não houver preferência salva
    if (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        body.setAttribute('data-theme', 'dark');
    }
}

// Adiciona animações de entrada aos elementos quando eles entram no viewport
function setupScrollAnimations() {
    const sections = document.querySelectorAll('section');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    sections.forEach(section => {
        section.classList.add('animate-on-scroll');
        observer.observe(section);
    });
}

// Atualiza as barras de progresso das habilidades
function updateSkillLevels() {
    const skillLevels = document.querySelectorAll('.skill-level');
    
    skillLevels.forEach(skill => {
        const level = skill.getAttribute('data-level');
        skill.style.width = `${level}%`;
    });
}

// Adiciona comportamento de rolagem suave aos links de navegação
function setupSmoothScroll() {
    const navLinks = document.querySelectorAll('nav a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Fecha o menu mobile se estiver aberto
            if (body.classList.contains('mobile-menu-active')) {
                body.classList.remove('mobile-menu-active');
            }
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 120, // Ajuste para o cabeçalho fixo
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Adiciona efeito de destaque ao cabeçalho durante a rolagem
function setupHeaderScroll() {
    const header = document.querySelector('header');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
}

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    // Inicializa o tema
    initTheme();
    
    // Configura as animações de rolagem
    setupScrollAnimations();
    
    // Atualiza as barras de progresso
    updateSkillLevels();
    
    // Configura a rolagem suave
    setupSmoothScroll();
    
    // Configura o efeito do cabeçalho na rolagem
    setupHeaderScroll();
    
    // Event listener para o botão de alternar tema
    themeToggleBtn.addEventListener('click', toggleTheme);
    
    // Event listener para o botão de menu
    menuToggleBtn.addEventListener('click', toggleMenu);
});

// Fecha o menu mobile quando a janela é redimensionada para um tamanho maior
window.addEventListener('resize', () => {
    if (window.innerWidth > 768 && body.classList.contains('mobile-menu-active')) {
        body.classList.remove('mobile-menu-active');
    }
});
