document.addEventListener("DOMContentLoaded", () => {
    //Aguardando o document carregar completamente antes de executar o código
    // --- 1. CAPTURA DE ELEMENTOS ---

    // Elementos do Formulário de cadastro

    const form_cadastro = document.getElementById("cadastro");
    const id_nome = document.getElementById("name");
    const id_email = document.getElementById("email");
    const id_senha = document.getElementById("senha");
    const id_confirmar_senha = document.getElementById("confirmar-senha");

    // Elementos da seção de testar o XSS

    const form_antixss = document.getElementById("anti-xss");
    const id_textoXSS = document.getElementById("email-anti-xss");
    const id_ver_email_semXSS = document.getElementById("ver-email-semXSS");
    const id_ver_email_comXSS = document.getElementById("ver-email-comXSS");

   

    form_cadastro.addEventListener("submit", (event) => {
        event.preventDefault(); // Impede o recarregamento da página
        
        const email = id_email.value.trim();
        const nome = id_nome.value.trim();
        const senha = id_senha.value.trim();
        const confirmarSenha = id_confirmar_senha.value.trim();
        console.log("Informações recebidas: Nome: ", nome, " Email: ", email, " Senha: ", senha);

        // --- Validação ---
        if (!nome || !email || !senha || !confirmarSenha) {
            alert("ERRO: Por favor, preencha todos os campos.");
            return; // Impede a execução do restante do código
        }
        if (senha !== confirmarSenha) {
            alert("ERRO: As senhas não coincidem.");
            return; // Impede a execução do restante do código
        }

        // Agora vamos validar se não existe algum código malicioso no campo de  nome
        const regex = /<script.*?>.*?<\/script>/i; // Regex simples para detectar tags de script
        if (regex.test(nome) ) {
            alert("ERRO: Código malicioso detectado em nome. Por favor, insira valores válidos.");
            return; // Impede a execução do restante do código
        }

        // Agora vamos supor que a validação passou e podemos prosseguir
        // Porém nao aplicamos o regex no e-mail, e agora?
        // Vamos adicionar 2 cenários possíveis, o que deve ser feito:
            // Quando for mostrar o e-mail na tela devemos usar textContent ou innerText
            // Quando for enviar o e-mail para o servidor, devemos usar encodeURIComponent para evitar XSS
            // NUNCA em HIPÓTESE ALGUMA devemos usar innerHTML com valores vindos de usuários
            // a não ser que tenhamos certeza absoluta de que o conteúdo é seguro (validação rigorosa)
            // e o mesmo deve ser feito ao servidor também, mesmo que outra validação seja feita lá.

        alert("Cadastro realizado com sucesso!");
        // Aqui seria o local de comunicação com a API, mas vamos testar na pratica o XSS
        form_antixss.classList.remove('hidden'); // Mostra a seção de teste de XSS
    });

    id_ver_email_comXSS.addEventListener("click", () => {
        // Exibe o e-mail com XSS (NÃO RECOMENDADO)
        id_textoXSS.innerHTML = id_email.value; // Isso pode causar XSS se o usuário inserir código malicioso
    
        // para testar, cole o seguinte código no campo de e-mail:
        // teste@email.com<img src="x" onerror="alert('XSS: Você foi atacado com imagem!');">
        // Isso deve disparar um alerta se o XSS for bem-sucedido
        // NUNCA FAÇA ISSO EM PRODUÇÃO!
    });

    id_ver_email_semXSS.addEventListener("click", () => {
        // Exibe o e-mail sem XSS (RECOMENDADO)
        id_textoXSS.textContent = id_email.value; // Isso é seguro, pois não executa código HTML
    });


});