/* global bootstrap: false */
(function () {
  'use strict'
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle=\'tooltip\']'))
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})()

var tablecat;

function pagcat() {
 tablecat = $('#categoriashow table').DataTable({ });
}

$(document).ready(function() {
  console.log('ready categorias')
  pagcat()
});