function selectQuerySet(e, itemID, URL) {
    let select = $(e);
    select.find('option').remove().end();

    $.get(URL + itemID, function(queryset) {
        if ( queryset.length === 0 ){
            select.append(new Option("----------", ""));
        } else {
            select.append(new Option("Выберите...", ""));
            for(let i=0; i < queryset.length; i++) {
                select.append(new Option(queryset[i]['name'], queryset[i]['id']));
            }
        }
    });
}

function emptySelect(e) {
    let select = $(e);
    select.find('option').remove().end();
    select.append(new Option("---------", ""));
}


function changeUserName(e, itemID, URLUser) {
    let select = $(e).find('a');

    $.get(URLUser + itemID, function(queryset) {
        let userId = queryset[0]['id'];
        let full_name = queryset[0]['first_name'] + ' '+ queryset[0]['last_name'];

        if ( queryset.length === 0 ) {
            select.text('(не задано)');
        } else {
            select.text(full_name);
            select.attr('href', '/admin/user/detail/' + userId);
        }
    });
}

function changeUserPhone(e, itemID, URLUser) {
    let select = $(e).find('a');

    $.get(URLUser + itemID, function(queryset) {
        let phone = queryset[0]['phone'];

        if ( queryset.length === 0 ) {
            select.text('(не задано)');

        } else {
            select.attr('href', 'tel:' + phone);
            select.text(phone);
        }
    });
}

function changeToEmpty(e, itemID, URLUser) {
    let select = $(e).find('a');

    $.get(URLUser + itemID, function(queryset) {
        let phone = queryset[0]['phone'];

        if ( queryset.length === 0 ) {
            select.text('(не задано)');

        }
    });
}