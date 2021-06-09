function addHiddenForm(prefix, form_class, image_class=undefined, default_image=undefined) {
        // get first form
        let firstForm = form_class + ":first";

        // clone hidden form from the last form
        let hiddenForm = $(firstForm).clone(true);

        // set attrs name and id
        hiddenForm.find(":input").each(function () {

            let name = $(this).attr('name').replace(prefix + '-0-','');

            let id = 'id_' + name;

            // set new name and id
            $(this).attr({
                'name': name,
                'id': id,
            }).val('').removeAttr('checked');
        });

        // find img tag than set default image instead of current
        if (image_class) {
            hiddenForm.find("img").each(function () {
                $(this).attr("src", default_image);
                $(this).attr("alt", default_image);
            });
        }

        // hide form from page and set it before all forms
        hiddenForm.css('display', 'none');
        $(firstForm).before(hiddenForm);
    }

    function addNewForm(prefix, form_class, index_class) {

        let firstForm = form_class + ":first";
        let lastForm = form_class + ":last";
        let newForm = $(firstForm).clone(true);
        let selectTotalForms = $('#id_' + prefix + '-TOTAL_FORMS')
        let totalForms = selectTotalForms.val()
        let allForms = $(form_class + ":not(:hidden)");

        // get input
        newForm.find(':input').each(function () {
            let name = prefix + '-' + totalForms + '-' + $(this).attr('name');
            let id = 'id_' + name;

            // set new name and id
            $(this).attr({
                'name': name,
                'id': id
            }).val('').removeAttr('checked');
        });

        // display current form
        newForm.css('display', '')

        // increment number
        totalForms++;

        // set TOTAL_FORMS number
        selectTotalForms.val(totalForms);

        // set last index
        newForm.find(index_class).each(function() {
            $(this).text(totalForms);
        });

        // set new form after last form
        $(lastForm).after(newForm);

        // cycle for updating all indexes of forms
        for (let i = 0, count = allForms.length; i < count; i++) {

            // get form
            let form = $(allForms.get(i));

            // set counter of form at the top of form
            if (index_class) form.find("span.form-index").text(i+1);

            // find input area and start updateFormIndex() for each
            form.find(":input").each(function () {
                updateFormIndex(form, prefix, i-1);
            });
        }
        let newFormId = newForm.find('textarea').attr('id')
        tinymce.init({
            selector: '#' + newFormId,
        });
    }

    function updateFormIndex(form, prefix, index) {
        let idRegex = new RegExp('(' + prefix + '-\\d+)');
        let replacement = prefix + '-' + index;
        let name = $(this).attr('name').replace(idRegex, replacement);
        let id = 'id_' + name;

        $(form).attr({
            'name': name,
            'id': id,
        }).val('');
    }

    function deleteForm(e, prefix, form_class, index_class=undefined) {

        // set checked to delete form after confirm
        $(e.target).siblings(".check_delete").children().prop('checked', true);
        // console.log($(e.target).siblings(".check_delete").children().prop('checked',true));
        // hide form on page
        $(e.target).parents(form_class).css("display", 'none');

        //set attr hidden to hide from selector
        $(e.target).parents(form_class).prop("hidden", true);

        // get all forms which not hidden
        let allForms = $(form_class + ":not(:hidden)");

        let selectTotalForms = $('#id_' + prefix + '-TOTAL_FORMS')

        // get number of all forms
        let totalForms = selectTotalForms.val() - 1;

        // set new number of all forms
        selectTotalForms.val(totalForms);

        // cycle for updating all indexes of forms
        for (let i = 0, count = allForms.length; i < count; i++) {

            // get form
            let form = $(allForms.get(i));

            // set counter of form at the top of form
            if (index_class) form.find("span.form-index").text(i+1);

            // find input area and start updateFormIndex() for each
            form.find(":input").each(function () {
                updateFormIndex(form, prefix, i-1);
            });
        }
    }