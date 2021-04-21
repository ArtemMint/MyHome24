function addHiddenForm(prefix, form_class, image_class, default_image_url) {
    let selector = form + ":first";
    let element = $(selector).clone(true);

    element.find(':input').each(function() {
        let name = $(this).attr('name').replace(prefix + '-0-', '');
        let id = 'id_' + name;
        $(this).attr({
            'name': name,
            'id': id
        }).val('').removeAttr('checked');
    });
    element.find("img").each(function() {
        $(this).attr("src", default_image_url);
    });
    element.css('display', 'none');
    $(selector).before(element);
}

function addNewForm(prefix, form, index) {
    let selector_first = form + ":first";
    let selector_last = form + ":last";
    let newElement = $(selector_first).clone(true);
    let total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    let i = 0;

    newElement.find(':input').each(() => {
        let name = prefix + '-' + total + '-' + $(this).attr('name');
        let id = 'id_' + name;
        $(this).attr({ 'name': name, 'id': id }).val('').removeAttr('checked');
    });
    newElement.css('display', '')

    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    if (index) newElement.find(index).each(() => { $(this).text(total); });
    $(selector_last).after(newElement);
}

function updateFormIndex(element, prefix, index) {
    let id_regex = new RegExp('(' + prefix + '-\\d+)');
    let replacement = prefix + '-' + index;
    let name = $(element.target).attr('name').replace(id_regex, replacement);
    let id = 'id_' + name;
    $(this).attr({ 'name': name, 'id': id }).val('');
};

function deleteForm(event, id, prefix, form, image, index) {

    $(event.target).parents(form).remove(); // delete forms and child tags

    const allForms = $(form); //
    const totalForms = $(id + prefix + '-TOTAL_FORMS').val() - 1;
    $(id + prefix + '-TOTAL_FORMS').val(totalForms);

    for (let i = 1, count = allForms.length; i < count; i++) {
        element = $(allForms.get(i));
        element.find(':input').each(() => {
            updateFormIndex(element, prefix, i - 1)
        });
        element.find("span").text(i);
    }
    return false;
};