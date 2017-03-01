$(document).ready(function() {
  app.
    route('/', function() {}).
    route('/fornecedores/', function() {
      app.utils.index('/fornecedores/', 'Excluir Fornecedor', 'Deseja realmente excluir este fornecedor?');
    }).
    route('/fornecedores/adicionar/', function() {
      console.log(':)');
      services.city($('#city_id'));
      validators.mask();
      validators.provider($('#provider'));
    }).
    route('/fornecedores/editar/:id', function() {
      services.city($('#city_id'));
      validators.mask();
      validators.provider($('#provider'));
    }).
    route('/usuarios/', function() {
      app.utils.index('/usuarios/', 'Excluir Usuário', 'Deseja realmente excluir este usuário?');
    }).
    route('/usuarios/adicionar/', function() {
      validators.mask();
      validators.user($('#user'));
    }).
    route('/usuarios/editar/:id', function() {
      validators.mask();
      validators.user($('#user'));
    });
  app.config.ajax();
  app.utils.back();
  app.run();
});
