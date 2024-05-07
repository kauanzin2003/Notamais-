document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que o formulário seja enviado normalmente

    const inputData = document.getElementById('inputData').value;

    // Faz uma requisição POST para a API com os dados inseridos no formulário
    fetch('http://127.0.0.1:5000/notas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=UTF-8',
        },
        body: JSON.stringify({ data: inputData }),
    })
    .then(response => response.json())
    .then(data => {
        if ('notas' in data && inputData.length == 6) {
            const arrayDoJson = data.notas;
            const notasDoAluno = arrayDoJson.filter(nota => nota[1] == inputData);

            if (notasDoAluno.length > 0) {
                const table = document.createElement('table');
                const tbody = document.createElement('tbody');
                if(notasDoAluno.length <2){
                table.classList.add('table', 'table-bordered', 'table-grey', 'table-striped');
                tbody.classList.add('table', 'table-bordered', 'table-grey', 'table-striped');

            }else{
                table.classList.add('table', 'table-bordered', 'table-grey', 'table-striped');
                tbody.classList.add('table', 'table-bordered', 'table-grey', 'table-striped');
            }
                notasDoAluno.forEach(nota => {
                    const row = document.createElement('tr');
                    const cell1 = document.createElement('td');
                    const cell2 = document.createElement('td');
                    const cell3 = document.createElement('td');

                    cell1.textContent = 'Nota: ' + nota[0];
                    cell2.textContent = 'RA: ' + nota[1];
                    cell3.textContent = nota[0] >= 6 ? 'Aprovado' : 'Reprovado';

                    row.appendChild(cell1);
                    row.appendChild(cell2);
                    row.appendChild(cell3);
                    tbody.appendChild(row);
                });

                table.appendChild(tbody);

                const resultTable = document.getElementById('resultTable');
                resultTable.innerHTML = '';
                resultTable.appendChild(table);
            } else {
                const resultTable = document.getElementById('resultTable');
                resultTable.innerHTML = ''; // Limpa o conteúdo
                resultTable.innerText = 'Aluno não encontrado ou sem notas registradas';
                alert('Aluno não encontrado ou sem notas registradas');
            }
        } else {
            const resultTable = document.getElementById('resultTable');
            resultTable.innerHTML = ''; // Limpa o conteúdo
            resultTable.innerText = 'Erro ao obter notas ou entrada inválida';
            alert('Erro ao obter notas ou entrada inválida');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        const resultTable = document.getElementById('resultTable');
        resultTable.innerHTML = ''; // Limpa o conteúdo
        resultTable.innerText = 'Erro ao conectar com o servidor';
    });
});

document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que o formulário seja enviado normalmente

    const inputData = document.getElementById('inputData').value;
})

    // Faz uma requisição POST para a API com os dados inseridos no formulário
    fetch('http://127.0.0.1:5000/crianota', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=UTF-8',
        },
        body: JSON.stringify({ data: inputData }),
})
