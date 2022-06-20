/* global bootstrap: false */
(function () {
  'use strict'
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle=\'tooltip\']'))
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})()

var tablelivro;

function paglivro() {
  tablelivro = $('#livroshow table').DataTable({ });
}

$(document).ready(function() {
  console.log('ready livros')
  paglivro()
});
