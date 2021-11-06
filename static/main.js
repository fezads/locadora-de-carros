jQuery(document).ready(function($) {
    const camposTelefone = $('[type=tel]');

    camposTelefone.each((index, campo) => {
        campo = $(campo);

        if (campo.val()) {
            campo.val(campo.val().replace('-', ''));
        }

        campo.inputmask({
            mask: () => {
                return ["(99) 9999-9999", "(99) 99999-9999"];
            },
            keepStatic: true,
            clearIncomplete: true,
            jitMasking: true,
        });
    });

    $('[data-cpf]').inputmask({
        mask: '999.999.999-99',
        clearIncomplete: true,
        jitMasking: true,
    });

    $('[data-email]').inputmask({
        mask: "*{1,20}[.*{1,20}][.*{1,20}][.*{1,20}]@*{1,20}.*{2,16}[.*{1,2}]",
        greedy: false,
        jitMasking: true,
        clearIncomplete: true,
        onBeforePaste: (pastedValue) => {
            pastedValue = pastedValue.toLowerCase();
            return pastedValue.replace("mailto:", "");
        },
        definitions: {
            '*': {
                validator: "[0-9A-Za-z!#$%&'*+/=?^_`{|}~\-]",
                casing: "lower"
            }
        }
    });

    // Inputmask("(.999){+|1},00", {
    //     positionCaretOnClick: "radixFocus",
    //     radixPoint: ",",
    //     _radixDance: true,
    //     numericInput: true,
    //     placeholder: "0",
    //     definitions: {
    //         "0": {
    //             validator: "[0-9\uFF11-\uFF19]"
    //         }
    //     }
    // }).mask(selector);

    $('#aviso-deletar').on('shown.bs.modal', (e) => {
        const link = $(e.relatedTarget).data('href');

        $(this).find('[data-botao-deletar]').attr('href', link);
    });
});