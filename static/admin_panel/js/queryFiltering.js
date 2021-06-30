function selectQuerySet(e, itemID, URL) {
    let select = $(e);
    select.find('option').remove().end();
    select.append(new Option("Выберите...", ""));
    $.get(URL + itemID, function(queryset) {
        for(let i=0; i < queryset.length; i++) {
            select.append(new Option(queryset[i]['name'], queryset[i]['id']));
        }
    });
}

function emptySelect(e) {
    let select = $(e);
    select.find('option').remove().end();
    select.append(new Option("---------", ""));
}