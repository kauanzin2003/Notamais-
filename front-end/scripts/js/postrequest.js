document.getElementById("form-nota").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    const data = {};

    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Remova a configuração 'Content-Type' e deixe o navegador configurá-lo automaticamente
    // Remova o JSON.stringify() do corpo da solicitação, pois os dados são enviados como FormData
    fetch('http://127.0.0.1:5000/crianota', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao cadastrar nota');
        }
        return response.json();
    })
    .then(data => {
        console.log(data.message); 
        alert('Nota cadastrada com sucesso!');
        location.reload();
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});
