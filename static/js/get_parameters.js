/*
This the first js
*/

function get_throughput(){
    var throughput_val = document.getElementsByName('throughput');

    for (var i = 0, length = throughput_val.length; i < length; i++) {
        if (throughput_val[i].checked) {
            console.log(throughput_val[i].value);

        }
    }

}