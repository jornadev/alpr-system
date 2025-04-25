function atualizarAutorizacoes() {
    fetch('/autorizacoes')
        .then(response => response.json())
        .then(data => {
            const lista = document.getElementById('listaAutorizacoes');
            lista.innerHTML = '';
            data.forEach(item => {
                const li = document.createElement('li');
                li.textContent = `Placa: ${item.placa} - Proprietário: ${item.proprietario}`;
                lista.appendChild(li);
            });
        });
}

function atualizarHistorico() {
    fetch('/historico')
        .then(response => response.json())
        .then(data => {
            const lista = document.getElementById('listaHistorico');
            lista.innerHTML = '';
            data.forEach(item => {
                const li = document.createElement('li');
                li.textContent = `Placa: ${item.placa} - Proprietário: ${item.proprietario} - Entrada: ${item.horario_entrada}`;
                lista.appendChild(li);
            });
        });
}

function adicionarPlaca() {
    const placa = document.getElementById('novaPlaca').value;
    const proprietario = document.getElementById('proprietario').value;

    fetch('/adicionar_placa', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ placa, proprietario })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.status === 'success') {
            atualizarAutorizacoes();
            document.getElementById('novaPlaca').value = '';
            document.getElementById('proprietario').value = '';
        }
    });
}

function removerPlaca() {
    const placa = document.getElementById('placaRemover').value;

    fetch('/remover_placa', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ placa })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.status === 'success') {
            atualizarAutorizacoes();
            document.getElementById('placaRemover').value = '';
        }
    });
}

function mostrarSecao(secao) {
    document.getElementById('autorizacoes').style.display = 'none';
    document.getElementById('historico').style.display = 'none';
    document.getElementById(secao).style.display = 'block';
}

document.addEventListener('DOMContentLoaded', () => {
    atualizarAutorizacoes();
    atualizarHistorico();
});
