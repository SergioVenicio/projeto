var l = document.location,
  base = l.protocol+'//'+l.hostname+(l.port ? ':'+l.port : '')+'/';

var services = {
  provider: function(el) {
    $(el).selectize({
      valueField: 'id',
      labelField: 'name',
      searchField: 'name',
      options: [],
      create: function(input, callback) {
        app.utils.modal.frame({'url': base+'fornecedores/adicionar/?name='+input});
        return callback({'id': '', 'name': ''});
      },
      render: {
        item: function(item, escape) {
          if (item.cnpj) {
            return '<div>' + escape(item.name) + ' - ' + escape(item.cnpj) + '</div>';
          } else {
            return '<div>' + escape(item.name) + '</div>';
          }
        },
        option: function(item, escape) {
          if (item.cnpj) {
            return '<div>' + escape(item.name) + ' - ' + escape(item.cnpj) + '</div>';
          } else {
            return '<div>' + escape(item.name) + '</div>';
          }
        },
        option_create: function(item, escape) {
          return '<div><i class="fa fa-plus"></i><strong> Adicionar não listado</strong>&hellip;</div>';
        }
      },
      load: function(query, callback) {
        if (!query.length) return callback();
        app.service.get({'action': base+'empresas/?select=1&search='+query}, function(response) {
          if (response.status) {
            callback(response.data.companies);
          } else {
            callback();
          }
        });
      },
      onChange: function (value) {
        var control = $(this.$wrapper).parent();
        if (control.hasClass('has-error')) {
          control.find('.help-block').hide();
          control.removeClass('has-error');
        }
      }
    });
  },

  city: function(el) {
    $(el).selectize({
      valueField: 'id',
      labelField: 'description',
      searchField: 'description',
      options: [],
      create: false,
      render: {
        item: function(item, escape) {
          if (item.state) {
            return '<div>' + escape(item.description) + ' - ' + escape(item.state) + '</div>';
          } else {
            return '<div>' + escape(item.description) + '</div>';
          }
        },
        option: function(item, escape) {
          if (item.state) {
            return '<div>' + escape(item.description) + ' - ' + escape(item.state) + '</div>';
          } else {
            return '<div>' + escape(item.description) + '</div>';
          }
        }
      },
      load: function(query, callback) {
        if (!query.length) return callback();
        app.service.get({'action': base+'cidades/?search='+query}, function(response) {
          if (response.status) {
            callback(response.data.cities);
          } else {
            callback();
          }
        });
      },
      onChange: function (value) {
        var control = $(this.$wrapper).parent();
        if (control.hasClass('has-error')) {
          control.find('.help-block').hide();
          control.removeClass('has-error');
        }
      }
    });
  },

  user: function(el) {
    $(el).selectize({
      valueField: 'id',
      labelField: 'name',
      searchField: 'name',
      options: [],
      create: false,
      load: function(query, callback) {
        if (!query.length) return callback();
        app.service.get({'action': base+'usuarios/?select=1&search='+query}, function(response) {
          if (response.status) {
            callback(response.data.users);
          } else {
            callback();
          }
        });
      },
      onChange: function (value) {
        var control = $(this.$wrapper).parent();
        if (control.hasClass('has-error')) {
          control.find('.help-block').hide();
          control.removeClass('has-error');
        }
      }
    });
  },

  date: function() {
    $('.date').datetimepicker({
      locale: 'pt-br'
    });
  }
};
