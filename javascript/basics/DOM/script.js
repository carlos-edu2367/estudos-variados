
// Esperando o DOM carregar
document.addEventListener("DOMContentLoaded", () =>{
    //Pegando formulário e campos
    const form = document.getElementById("form-ganhos");
    const salarioInput = document.getElementById("salario");
    const idadeInput = document.getElementById("idade");
    const mora_com_paisInput = document.getElementById("mora-com-pais");
    //Pegando section de resultados
    const section_resultados = document.getElementById("results");
    const id_invest = document.getElementById("investir");
    const id_despesas = document.getElementById("despesas");
    const id_guardar = document.getElementById("reservas");
    const id_recompensas = document.getElementById("recompensas");

    // Espera o botão submit do form ser clicado
    form.addEventListener("submit", (event) =>{
        event.preventDefault(); //Impede o recarregamento da página


        //Tomar muito cuidado ao tratar inputs, pois eles vem em formato html, quando
        //vamos pegar os números devemos sempre passar o método .value
        const salario = parseFloat(salarioInput.value); // converte para float
        const idade = parseInt(idadeInput.value); // converte para int
        const mora_com_pais = mora_com_paisInput.checked; //.checked verifica se o check é true ou false

        console.log("Informações recebidas: Salário: R$ ", salario, " Idade: ", idade, " Mora com os pais? ", mora_com_pais);
        //Depurando a passagem e formato de dados.

        let investimentos, despesas, reserva, recompensas;
        if(!isNaN(salario) && !isNaN(idade)){ 
            //isNaN verifica se a variavel não é um numero, se for um numero retorna falso
            // por isso a inversão com !, agora ela retorna true se for um numero

            // Iniciando calculo de divisão de ganhos
            
            if (mora_com_pais){
                //Se mora com os pais pode investir 30% do seu salário (acima da media)
                investimentos = salario*0.3;
                despesas = salario*0.4;
                reserva = salario*0.20;
                recompensas = salario*0.10;
            } else{
                //Se não mora com os pais devemos verificar algumas outras cases
                if (salario>4000){
                    investimentos = salario*0.25;
                    despesas = salario*0.5;
                    reserva = salario*0.15;
                    recompensas = salario*0.1;
                }else{
                    investimentos = salario*0.20;
                    despesas = salario*0.6;
                    reserva = salario*0.15;
                    recompensas = salario*0.05;
                }

            }
        } else{
            console.log("ERRO: Por favor digite valores validos");
        }
        console.log("O que recomendamos para você é:");
        console.log("Invista R$ ", investimentos, " por mês");
        console.log("Use R$ ", despesas, " para pagar suas despesas");
        console.log("Guarde R$ ", reserva, " em sua reserva de emergência");
        console.log("Use R$ ", recompensas, " como recompensas");

        //Iniciando o processo de mostrar resultados
        //Passo 1 - Esconder o form e mostrar a section
        // utilizando .classList para adicionar/remover uma classe ao elemento html

        form.classList.add('hidden');
        section_resultados.classList.remove('hidden');

        //Passo 2 - Modificar os valores no dashboard para os calculados
        //Utilizando .textContent para modificar o texto de algum elemento html
        id_invest.textContent = "R$ " + investimentos.toFixed(2);
        id_despesas.textContent = "R$ " + despesas.toFixed(2);
        id_guardar.textContent = "R$ " + reserva.toFixed(2);
        id_recompensas.textContent = "R$ " + recompensas.toFixed(2);

        // Atenção!! textContent não é uma função, ele é uma forma de atributo
        // ou seja, se passar o resultado assim: .textContent(resultado) nao funciona
        // deve ser passado atribuindo um valor.


    })
});