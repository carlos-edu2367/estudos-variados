// Esperando o DOM carregar
document.addEventListener("DOMContentLoaded", () => {
    // --- 1. CAPTURA DE ELEMENTOS ---
    // (Melhor agrupado para clareza)

    // Elementos do Formulário Principal
    const formGanhos = document.getElementById("form-ganhos"); 
    const salarioInput = document.getElementById("salario");
    const idadeInput = document.getElementById("idade");
    const moraComPaisInput = document.getElementById("mora-com-pais"); 

    // Elementos da Seção de Resultados do Plano Financeiro
    const sectionResultados = document.getElementById("results"); 
    const idInvestir = document.getElementById("investir"); 
    const idDespesas = document.getElementById("despesas"); 
    const idReservas = document.getElementById("reservas"); 
    const idRecompensas = document.getElementById("recompensas"); 

    // Elementos do Formulário de Juros e Seção de Detalhes do Investimento
    const numeroAnosInput = document.getElementById("numero-de-anos"); 
    const formJuros = document.getElementById("form-juros"); 

    const sectionDetalhesInvestimentos = document.getElementById("detalhes-investimento"); // Renomeado
    const displayValorTotal = document.getElementById("valor-total"); 
    const displayValorAportado = document.getElementById("valor-total-aportado"); 
    const displayValorTotalJuros = document.getElementById("total-juros"); 
    const displayAnosAporte = document.getElementById("anos-de-aporte"); 

    // --- VARIÁVEIS PARA ARMAZENAR RESULTADOS (ACESSÍVEIS GLOBALMENTE OU PASSADOS) ---
    // Estas variáveis armazenarão os resultados do primeiro cálculo
    // e precisarão ser acessíveis ao segundo event listener.
    // Vamos declará-las aqui no escopo mais alto do DOMContentLoaded.
    let investimentosMensal = 0; // Armazenará o valor de 'investimentos' do primeiro cálculo


    // --- 2. PRIMEIRO EVENT LISTENER: FORMULÁRIO PRINCIPAL (form-ganhos) ---
    formGanhos.addEventListener("submit", (event) => {
        event.preventDefault(); // Impede o recarregamento da página

        const salario = parseFloat(salarioInput.value);
        const idade = parseInt(idadeInput.value);
        const moraComPais = moraComPaisInput.checked;

        console.log("Informações recebidas: Salário: R$ ", salario, " Idade: ", idade, " Mora com os pais? ", moraComPais);

        // --- Validação ---
        if (isNaN(salario) || isNaN(idade) || salario <= 0 || idade <= 0) {
            console.log("ERRO: Por favor, digite valores numéricos válidos e maiores que zero para Salário e Idade.");
            // Opcional: Mostrar uma mensagem de erro no HTML aqui
            // E esconder as seções de resultado se elas estiverem visíveis
            sectionResultados.classList.add('hidden');
            sectionDetalhesInvestimentos.classList.add('hidden');
            return; // Impede a execução do restante do código
        }

        // --- Lógica de cálculo de divisão de ganhos ---
        let despesas, reserva, recompensas;

        if (moraComPais) {
            investimentosMensal = salario * 0.3; // Atribuindo ao 'investimentosMensal' global
            despesas = salario * 0.4;
            reserva = salario * 0.20;
            recompensas = salario * 0.10;
        } else {
            if (salario > 4000) {
                investimentosMensal = salario * 0.25; // Atribuindo ao 'investimentosMensal' global
                despesas = salario * 0.5;
                reserva = salario * 0.15;
                recompensas = salario * 0.1;
            } else {
                investimentosMensal = salario * 0.20; // Atribuindo ao 'investimentosMensal' global
                despesas = salario * 0.6;
                reserva = salario * 0.15;
                recompensas = salario * 0.05;
            }
        }

        // --- Exibir resultados do plano financeiro no HTML ---
        formGanhos.classList.add('hidden'); // Esconde o formulário principal
        sectionDetalhesInvestimentos.classList.add('hidden'); // Garante que a seção de juros esteja escondida
        sectionResultados.classList.remove('hidden'); // Mostra a seção de resultados do plano

        idInvestir.textContent = "R$ " + investimentosMensal.toFixed(2);
        idDespesas.textContent = "R$ " + despesas.toFixed(2);
        idReservas.textContent = "R$ " + reserva.toFixed(2);
        idRecompensas.textContent = "R$ " + recompensas.toFixed(2);

        // Logs para depuração (opcional, pode remover no final)
        console.log("O que recomendamos para você é:");
        console.log("Invista R$ ", investimentosMensal.toFixed(2), " por mês");
        console.log("Use R$ ", despesas.toFixed(2), " para pagar suas despesas");
        console.log("Guarde R$ ", reserva.toFixed(2), " em sua reserva de emergência");
        console.log("Use R$ ", recompensas.toFixed(2), " como recompensas");

        // O cálculo de juros e sua exibição agora serão acionados PELO SEGUNDO FORMULÁRIO.
        // Isso é crucial para que os valores de juros sejam re-calculados e exibidos quando o usuário
        // clicar no botão "Quanto terei?".
    });


    // --- 3. SEGUNDO EVENT LISTENER: FORMULÁRIO DE JUROS (form-juros) ---
    // ESTE LISTENER NÃO ESTÁ MAIS ANINHADO. Ele é independente.
    formJuros.addEventListener("submit", (event) => {
        event.preventDefault(); // Impede o recarregamento da página

        const anosSimulacao = parseInt(numeroAnosInput.value); // Pega o valor do input de anos

        // Validação para anos de simulação
        if (isNaN(anosSimulacao) || anosSimulacao <= 0) {
            console.error("ERRO: Por favor, insira um número válido e positivo para a quantidade de anos para simulação.");
            // Opcional: Exibir essa mensagem no HTML também
            return; // Para não prosseguir com o cálculo de juros inválido
        }

        // --- CÁLCULO DE JUROS COMPOSTOS AGORA AQUI DENTRO ---
        // Agora, 'investimentosMensal' (do escopo superior) está acessível e tem o valor do primeiro cálculo.

        let mesesConvertidos = anosSimulacao * 12;

        // Inicialização correta para o cálculo de juros
        let valorTotalJurosSimulacao = investimentosMensal; // Começa com o primeiro aporte
        let valorTotalmenteAportadoSimulacao = investimentosMensal; // Total aportado sem juros

        // Se investimentosMensal for 0 (caso o primeiro form não tenha sido preenchido corretamente),
        // isso resultará em 0. É uma boa ideia validar isso também.
        if (investimentosMensal <= 0) {
            console.warn("Nenhum valor de investimento mensal definido. Por favor, preencha o formulário principal primeiro.");
            // Você pode exibir uma mensagem para o usuário aqui.
            return;
        }

        for (let i = 0; i < mesesConvertidos; i++) { // 'let i' para escopo correto
            valorTotalJurosSimulacao = valorTotalJurosSimulacao * 1.01; // Aplica juros (1% ao mês)
            valorTotalJurosSimulacao = valorTotalJurosSimulacao + investimentosMensal; // Adiciona novo aporte
            valorTotalmenteAportadoSimulacao = valorTotalmenteAportadoSimulacao + investimentosMensal; // Acumula aportes
            // O console.log de 'repetiu i' pode ser removido agora
        }

        // Calcula os juros acumulados apenas NO FINAL do loop
        let jurosAcumuladosSimulacao = valorTotalJurosSimulacao - valorTotalmenteAportadoSimulacao;

        // Logs para depuração
        console.log("--- Simulação de Investimento ---");
        console.log("Total Aportado na Simulação: R$", valorTotalmenteAportadoSimulacao.toFixed(2));
        console.log("Total com Juros na Simulação: R$", valorTotalJurosSimulacao.toFixed(2));
        console.log("Juros Acumulados na Simulação: R$", jurosAcumuladosSimulacao.toFixed(2));

        // --- Exibir resultados da simulação de investimento no HTML ---
        sectionResultados.classList.add("hidden"); // Esconde a seção de resultados do plano
        sectionDetalhesInvestimentos.classList.remove("hidden"); // Mostra a seção de detalhes

        displayValorAportado.textContent = valorTotalmenteAportadoSimulacao.toFixed(2);
        displayValorTotal.textContent = valorTotalJurosSimulacao.toFixed(2);
        displayValorTotalJuros.textContent = jurosAcumuladosSimulacao.toFixed(2);
        displayAnosAporte.textContent = anosSimulacao; // ATUALIZA O NÚMERO DE ANOS!
    });
});