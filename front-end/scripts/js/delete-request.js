document.getElementById('btn').addEventListener('click', function() {
    const idNota = document.getElementById('id_nota').value;

    // Faz uma requisição DELETE para a API para excluir a nota com base no ID fornecido
    fetch(`http://127.0.0.1:5000/excluir/${idNota}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Erro ao excluir a nota');
    })
    .then(data => {
        console.log(data.message);
        alert('Nota deletada com sucesso!');
        // Faça qualquer outra ação necessária, como recarregar a página ou atualizar a lista de notas
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao excluir a nota');
    });
});
