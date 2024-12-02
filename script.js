let consultas = [];

document.getElementById('consulta-form').addEventListener('submit', function(e) {
  e.preventDefault();

  const paciente = document.getElementById('paciente').value;
  const medico = document.getElementById('medico').value;
  const data = document.getElementById('data').value;
  const horario = document.getElementById('horario').value;
  const especialidade = document.getElementById('especialidade').value;

  const novaConsulta = { paciente, medico, data, horario, especialidade };
  consultas.push(novaConsulta);
  atualizarLista();
  this.reset();
});

function atualizarLista() {
  const lista = document.getElementById('consultas-list');
  lista.innerHTML = '';

  consultas.forEach((consulta, index) => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${consulta.paciente}</td>
      <td>${consulta.medico}</td>
      <td>${consulta.data}</td>
      <td>${consulta.horario}</td>
      <td>${consulta.especialidade}</td>
      <td class="actions">
        <button class="edit" onclick="editarConsulta(${index})">Editar</button>
        <button onclick="excluirConsulta(${index})">Excluir</button>
      </td>
    `;
    lista.appendChild(row);
  });
}

function editarConsulta(index) {
  const consulta = consultas[index];

  document.getElementById('paciente').value = consulta.paciente;
  document.getElementById('medico').value = consulta.medico;
  document.getElementById('data').value = consulta.data;
  document.getElementById('horario').value = consulta.horario;
  document.getElementById('especialidade').value = consulta.especialidade;

  excluirConsulta(index);
}

function excluirConsulta(index) {
  consultas.splice(index, 1);
  atualizarLista();
}