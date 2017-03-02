var l = document.location,
  base = l.protocol+'//'+l.hostname+(l.port ? ':'+l.port : '')+'/';

var services = {
  provider: function(el) {
    $(el).selectize({
      valueField: 'id',
      labelField: 'social_reason',
      searchField: 'social_reason',
      options: [],
      create: false,
      load: function(query, callback) {
        if (!query.length) return callback();
        app.service.get({'action': base+'fornecedores/?xhr=1&search='+query}, function(response) {
          if (response.status) {
            callback(response.data.providers);
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
