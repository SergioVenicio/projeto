jQuery.validator.setDefaults({
  ignore: ':hidden:not([class~=selectized]),:hidden > .selectizeded, .selectize-control .selectize-input input',
  highlight: function(element) {
    $(element).closest('.form-group').addClass('has-error');
  },
  unhighlight: function(element) {
    $(element).closest('.form-group').removeClass('has-error');
  },
  onfocusout: function(element) {
    this.element(element);
  },
  errorElement: 'span',
  errorClass: 'help-block',
  errorPlacement: function(error, element) {
    if(element.parent('.input-group').length) {
      error.insertAfter(element.parent());
    } else if (element.next('.selectize-control').length) {
      error.insertAfter(element.next('.selectize-control'));
    } else {
      error.insertAfter(element);
    }
  }
});

validators = {
  provider: function(form) {
    app.utils.enter_prevent();
    $(form).validate({
      rules: {
        social_reason: {
          minlength: 3,
          maxlength: 255,
          required: true
        },
        cnpj: {
          minlength: 17,
          maxlength: 18,
          required: true,
          cnpj: true
        },
        state_registration: {
          minlength: 10,
          maxlength: 25,
          required: true
        },
        address: {
          minlength: 3,
          maxlength: 255,
          required: true
        },
        district: {
          minlength: 3,
          maxlength: 60,
          required: true
        },
        city_id: {
          required: true
        },
        telephone: {
          required: true
        },
        email: {
          email: true
        }
      },
      messages: {
        social_reason: {
          minlength: 'A razão social deve possuir no mínimo {0} caracteres.',
          maxlength: 'A razão social deve possuir no máximo {0} caracteres.',
          required: 'Digite a razão social.'
        },
        cnpj: {
          minlength: 'O CNPJ deve possuir no mínimo {0} caracteres.',
          maxlength: 'O CNPJ deve possuir no máximo {0} caracteres.',
          required: 'Digite o CNPJ.'
        },
        state_registration: {
          minlength: 'A inscrição estadual deve possuir no mínimo {0} caracteres.',
          maxlength: 'A inscrição estadual deve possuir no máximo {0} caracteres.',
          required: 'Digite a inscrição estadual.'
        },
        address: {
          minlength: 'O endereço deve possuir no mínimo {0} caracteres.',
          maxlength: 'O endereço deve possuir no máximo {0} caracteres.',
          required: 'Digite o endereço.'
        },
        district: {
          minlength: 'O bairro deve possuir no mínimo {0} caracteres.',
          maxlength: 'O bairro deve possuir no máximo {0} caracteres.',
          required: 'Digite o bairro.'
        },
        city_id: {
          required: 'Selecione a cidade.'
        },
        telephone: {
          required: 'Digite o telefone.'
        },
        email: {
          email: 'Informe um email válido.'
        }
      }
    });
  },

  product: function(form) {
    app.utils.enter_prevent();
    $(form).validate({
      rules: {
        provider_id: {
          required: true
        },

        description: {
          maxlength: 100,
          required: true
        },

        unit: {
          maxlength: 2,
          required: true
        }
      },

      messages: {
        provider_id: {
          required: 'Digite o fornecedor.'
        },

        description: {
          maxlength: 'O login deve possuir no máximo {0} caracteres.',
          required: 'Digite a descrição do produto.'
        },

        unit: {
          maxlength: 'A unidade de media deve possuir no máximo {0} caracteres.',
          required: 'Digite a unidade de medida.'
        }
      }
    });
  },

  user: function(form) {
    app.utils.enter_prevent();
    $(form).validate({
      rules: {
        login: {
          minlength: 2,
          maxlength: 255,
          alphanumeric: true,
          required: true
        },
        name: {
          minlength: 2,
          maxlength: 255,
          required: true
        },
        rg: {
          minlength: 4,
          maxlength: 15,
          required: true,
          alphanumeric: true
        },
        cpf: {
          minlength: 13,
          maxlength: 14,
          required: true,
          cpf: true
        },
        location_id: {
          znumeric: true
        },
        telephone: {
          minlength: 14,
          maxlength: 15,
          required: true
        },
        email: {
          email: true
        },
        user_type_id: {
          znumeric: true
        },
        password: {
          minlength: 6,
          maxlength: 255,
          required: true
        }
      },
      messages: {
        login: {
          minlength: 'O login deve possuir no mínimo {0} caracteres.',
          maxlength: 'O login deve possuir no máximo {0} caracteres.',
          required: 'Digite o login.'
        },
        name: {
          minlength: 'O nome deve possuir no mínimo {0} caracteres.',
          maxlength: 'O nome deve possuir no máximo {0} caracteres.',
          required: 'Digite o nome.'
        },
        rg: {
          minlength: 'O RG deve possuir no mínimo {0} caracteres.',
          maxlength: 'O RG deve possuir no máximo {0} caracteres.',
          required: 'Digite o RG.'
        },
        cpf: {
          minlength: 'O CPF deve possuir no mínimo {0} caracteres.',
          required: 'Digite o CPF.'
        },
        location_id: {
          znumeric: 'Selecione uma localização.'
        },
        telephone: {
          minlength: 'O telefone deve possuir no mínimo {0} caracteres.',
          maxlength: 'O telefone deve possuir no máximo {0} caracteres.',
          required: 'Digite o telefone.'
        },
        email: {
          email: 'Informe um email válido.'
        },
        user_type_id: {
          znumeric: 'Selecione um tipo de usuário.'
        },
        password: {
          minlength: 'A senha deve possuir no mínimo {0} caracteres.',
          maxlength: 'A senha deve possuir no máximo {0} caracteres.',
          required: 'Digite a senha.'
        }
      }
    });
  },

  mask: function() {
    $('.cpf-mask').mask('999.999.999-?99');
    $('.cnpj-mask').mask('99.999.999/9999-9?9');
    $('.phone-mask').mask("(99) 9999-9999?9").on('change', function (event) {
      var target, phone, element;
      target = (event.currentTarget) ? event.currentTarget : event.srcElement;
      phone = target.value.replace(/\D/g, '');
      element = $(target);
      element.unmask();
      if(phone.length > 10) {
        element.mask("(99) 99999-999?9");
      } else {
        element.mask("(99) 9999-9999?9");
      }
    });
    $('.plate-mask').mask('aaa-9999');
  }
};

