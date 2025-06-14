document.addEventListener('DOMContentLoaded', () => {
    const submenuToggles = document.querySelectorAll('.has-submenu > a');
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    const clearButton = document.querySelector('.clear-button');
    const searchInput = document.querySelector('.search-container input');

    // Alternar submenu no clique
    submenuToggles.forEach((toggle) => {
        toggle.addEventListener('click', (e) => {
            e.preventDefault(); // Evita o comportamento padrão do link
            const submenu = toggle.nextElementSibling; // Seleciona o submenu relacionado
            submenu.classList.toggle('active'); // Alterna a classe active

            // Fecha outros submenus, se necessário
            submenuToggles.forEach((otherToggle) => {
                if (otherToggle !== toggle) {
                    const otherSubmenu = otherToggle.nextElementSibling;
                    otherSubmenu.classList.remove('active'); // Fecha outros submenus
                }
            });
        });
    });

    // Alternar menu hambúrguer no clique
    hamburgerMenu.addEventListener('click', () => {
        dropdownMenu.classList.toggle('active'); // Alterna a exibição do menu dropdown
    });

    // Botão de limpar campo de pesquisa
    if (clearButton && searchInput) {
        clearButton.addEventListener('click', () => {
            searchInput.value = ''; // Limpa o campo de pesquisa
            searchInput.focus(); // Foca novamente no campo
        });
    }
    

    // Dados completos do gráfico
const fullLabels = ['2019 /1', '2019 /2', '2020 /1', '2020 /2', '2021 /1', '2021 /2', '2022 /1', '2022 /2', '2023 /1', '2023 /2', '2024 /1', '2024 /2'];
const fullDataBlue = [250, 150, 90, 140, 110, 105, 130, 100, 60, 80, 90, 60];
const fullDataGreen = [90, 110, 115, 185, 170, 230, 200, 150, 175, 125, 190, 210];

// Dados reduzidos para telas menores
const mobileLabels = ['2023 /1', '2023 /2', '2024 /1', '2024 /2'];
const mobileDataBlue = [60, 80, 90, 60];
const mobileDataGreen = [175, 125, 190, 210];

let approvalChart;

// Função para criar ou atualizar o gráfico
function createOrUpdateChart(isMobile) {
    const ctx = document.getElementById('approvalChart').getContext('2d');

    // Remove o gráfico existente se houver
    if (approvalChart) {
        approvalChart.destroy();
    }

    // Define os dados com base no tamanho da tela
    const labels = isMobile ? mobileLabels : fullLabels;
    const dataBlue = isMobile ? mobileDataBlue : fullDataBlue;
    const dataGreen = isMobile ? mobileDataGreen : fullDataGreen;

    approvalChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Linha Azul',
                    data: dataBlue,
                    borderColor: 'rgba(0, 51, 102, 1)', // Azul escuro
                    backgroundColor: 'rgba(0, 51, 102, 0.1)', // Azul com transparência
                    fill: true, // Preencher área abaixo da linha
                    tension: 0.4, // Suavizar a curva
                },
                {
                    label: 'Linha Verde',
                    data: dataGreen,
                    borderColor: 'rgba(0, 161, 150, 1)', // Verde
                    backgroundColor: 'rgba(0, 161, 150, 0.1)', // Verde com transparência
                    fill: true, // Preencher área abaixo da linha
                    tension: 0.4, // Suavizar a curva
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false, // Oculta legenda
                }
            },
            scales: {
                x: {
                    grid: {
                        display: true,
                        color: '#E0E0E0'
                    }
                },
                y: {
                    grid: {
                        display: true,
                        color: '#E0E0E0'
                    },
                    ticks: {
                        stepSize: 50
                    }
                }
            }
        }
    });
}

// Função para verificar se o dispositivo é mobile
function checkIfMobile() {
    return window.innerWidth <= 768; // Define "mobile" como telas com largura de 768px ou menor
}

// Inicializa o gráfico com base no tamanho da tela
createOrUpdateChart(checkIfMobile());

// Adiciona um listener para mudanças no tamanho da tela
window.addEventListener('resize', () => {
    createOrUpdateChart(checkIfMobile());
});




});
