document.getElementById("form-atualizar").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);

    fetch('http://127.0.0.1:5000/editar/' + formData.get('idNota'), {
        method: 'PUT',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao atualizar nota');
        }
        return response.json();
    })
    .then(data => {
        console.log(data.message); 
        alert('Nota atualizada com sucesso!');
        location.reload();
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});