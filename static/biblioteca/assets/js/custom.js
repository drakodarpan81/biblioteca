$(function () {
    $("#id_fecha_publicacion").datetimepicker({dateFormat: 'dd/mm/yy', maxDate: 0, controlType: 'select'}).attr("autocomplete", "off");
});

$.timepicker.regional['es'] = {
    timeOnlyTitle: 'Elegir una hora',
    timeText: 'Hora',
    hourText: 'Horas',
    minuteText: 'Minutos',
    secondText: 'Segundos',
    millisecText: 'Milisegundos',
    microsecText: 'Microsegundos',
    timezoneText: 'Uso horario',
    currentText: 'Hoy',
    closeText: 'Cerrar',
    timeFormat: 'HH:mm',
    timeSuffix: '',
    amNames: [
        'a.m.', 'AM', 'A'
    ],
    pmNames: [
        'p.m.', 'PM', 'P'
    ],
    monthNames: [
        'Enero',
        'Febrero',
        'Marzo',
        'Abril',
        'Mayo',
        'Junio',
        'Julio',
        'Agosto',
        'Septiembre',
        'Octubre',
        'Noviembre',
        'Diciembre'
    ],
    monthNamesShort: [
        'Ene',
        'Feb',
        'Mar',
        'Abr',
        'May',
        'Jun',
        'Jul',
        'Ago',
        'Sep',
        'Oct',
        'Nov',
        'Dic'
    ],
    dayNames: [
        'Domingo',
        'Lunes',
        'Martes',
        'Miércoles',
        'Jueves',
        'Viernes',
        'Sábado'
    ],
    dayNamesShort: [
        'Dom',
        'Lun',
        'Mar',
        'Mié',
        'Juv',
        'Vie',
        'Sáb'
    ],
    dayNamesMin: [
        'Do',
        'Lu',
        'Ma',
        'Mi',
        'Ju',
        'Vi',
        'Sá'
    ],
    isRTL: false
};
$.timepicker.setDefaults($.timepicker.regional['es']);