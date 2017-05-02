var app = {
  config: {
    ajax: function() {
      var csrftoken = $('meta[name=csrf-token]').attr('content');
      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
          if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        }
      });
    }
  },

  routes: {},

  route: function(url, controller) {
    this.routes[url] = {'controller': controller};
    return this;
  },

  run: function() {
    try {
      path = window.location.pathname;
      select = {'url': '', 'max': 0};
      for (var url in this.routes) {
        match = path.match(new RegExp('^' + url.replace(/:([^\/]+)/g, '([^\/])*') + '$'));
        if (match instanceof Array) {
          if (match.length > select.max) {
            select.url = url;
            select.max = match.length;
          }
        }
      }
      return this.routes[select.url].controller();
    } catch (e) {}
  },

  service: {
    get: function(params, callback) {
      $.ajax({
        type: 'GET',
        url: params.action,
        headers: params.headers || '',
        data: params.data || '',
        success: function(data, status, xhr) {
          return callback({data: data, status: true, xhr: xhr});
        },
        error: function(data, status, xhr) {
          return callback({data: data, status: false, xhr: xhr});
        }
      });
    },

    save: function(params, callback) {
      $.ajax({
        type: 'POST',
        url: params.action,
        headers: params.headers || '',
        data: params.data || '',
        success: function(data, status, xhr) {
          return callback({data: data, status: true, xhr: xhr});
        },
        error: function(data, status, xhr) {
          return callback({data: data, status: false, xhr: xhr});
        }
      });
    },

    update: function(params, callback) {
      $.ajax({
        type: 'PUT',
        url: params.action,
        headers: params.headers || '',
        data: params.data || '',
        success: function(data, status, xhr) {
          return callback({data: data, status: true, xhr: xhr});
        },
        error: function(data, status, xhr) {
          return callback({data: data, status: false, xhr: xhr});
        }
      });
    },

    remove: function(params, callback) {
      $.ajax({
        type: 'DELETE',
        url: params.action,
        headers: params.headers || '',
        data: params.data || '',
        success: function(data, status, xhr) {
          return callback({data: data, status: true, xhr: xhr});
        },
        error: function(data, status, xhr) {
          return callback({data: data, status: false, xhr: xhr});
        }
      });
    },

    request: function(params, callback) {
      var methods = {
        'GET': 'get',
        'POST': 'save',
        'PUT': 'update',
        'DELETE': 'remove'
      };
      return app.service[methods[params.method]](params, callback);
    }
  },

  utils: {
    back: function(when) {
      $('.back').on('click', function() {
        parent.history.back();
      });
    },

    enter_prevent: function() {
      $('form input:not([type="submit"])').keydown(function(e) {
        if(e.keyCode == 13) {
          e.preventDefault();
          return false;
        }
      });
    },

    modal: {
      frame: function(params) {
        $('#content').attr('src', params.url);
        $('#content').load(function() {
          this.style.width = $('.modal-body').width() + 'px';
          this.style.height = this.contentWindow.document.body.offsetHeight + 'px';
        });
        $('#modal').modal('show');
      },
      service: function(params, callback) {
        //title, message, action, data, method
        var methods = {
          'GET': ['default', 'refresh'],
          'POST': ['primary', 'save'],
          'PUT': ['warning', 'warning'],
          'DELETE': ['danger', 'trash']
        },
        style = methods[params.method];

        // Formatação
        $('.modal-title').text(params.title);
        $('.modal-message').text(params.message);
        $('#yes').addClass('btn-' + style[0]);
        $('#icon').addClass('fa-' + style[1]);

        // Métodos
        $('#modal').modal('toggle');
        $('#modal').on('shown.bs.modal', function() {
          $('#yes').on('click', function() {
            return app.service.request(params, callback);
          });
        });
      },

      delete: function(title, message) {
        $('.delete').on('click', function() {
          var action = $(this).data('action');
          app.utils.modal.service({
            title: title,
            message: message,
            action: action,
            method: 'DELETE'
          }, function(response) {
            if (response.status) {
              window.location.reload();
              app.utils.modal.destroy();
            }
          });
        });
      },

      destroy: function() {
        $('#modal').modal('toggle');
        setTimeout(function() {
          $('#modal').remove();
        }, 500);
      }
    },

    upload_image: function(config) {
      if (!window.File && !window.FileList && !window.FileReader) {
        alert('O navegador não suporta a API de Arquivos!');
        return;
      }

      var preview = $(config.file_path).val(),
        setPreview = function(path) {
          $(config.preview).attr('src', path);
        };

      if (preview) setPreview(preview);

      $(config.upload_button).on('change', function(e) {
        var reader = new FileReader();
        reader.onload = (function(e) {
          setPreview(e.target.result);
        });
        reader.readAsDataURL(e.target.files[0]);
      });

      $(config.remove_button).on('click', function() {
        $(config.upload_button).val('');
        $(config.file_path).val('');
        setPreview(config.fallback_image);
      });
    },

    index: function(service, title, message) {
      $('#search').on('keyup', function() {
        var self = $(this),
          url;
        if (self.val() !== '') {
          url = service + '?search=' + self.val() + ' #data';
          $('.search').addClass('hide');
          $('.clean-search').removeClass('hide');
          $('.clean-search').on('click', function() {
            self.val('');
            self.trigger('keyup');
          });
        } else {
          url = service + ' #data';
          $('.clean-search').addClass('hide');
          $('.search').removeClass('hide');
        }
        $('#grid').load(url, function() {
          app.utils.modal.delete(title, message);
        });
      });
      app.utils.modal.delete(title, message);
    }
  }
};
