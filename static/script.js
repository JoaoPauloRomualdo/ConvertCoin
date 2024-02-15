document.addEventListener("DOMContentLoaded", function () {
  // Simula o carregamento dos recursos (pode ser substituído por chamadas assíncronas reais)
  setTimeout(function () {
    // Esconde o preloader quando os recursos estiverem carregados
    document.getElementById("preloader").style.display = "none";
  }, 1000); // Tempo de simulação (em milissegundos)
});


function mostrarDivFlutuante(id) {
  var divFlutuante = document.getElementById(id);
  divFlutuante.style.display = "block";
}

function fecharDivFlutuante(id) {
  var divFlutuante = document.getElementById(id);
  divFlutuante.style.display = "none";
}
