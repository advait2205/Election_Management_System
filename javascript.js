var candidates = `[
    {
        "name": "Dev Choganwala",
        "position": "CEO",
        "region": "Gujarat",
        "votes": "10000"
    },
    {
        "name": "Bread Butter",
        "position": "CFO",
        "region": "Rajasthan",
        "votes": "10"
    },
    {
        "name": "Cha pani",
        "position": "EC",
        "region": "Maharashtra",
        "votes": "12"
    }
]`;

function search(value) {
    f = value;
    var reg = " ", pos = " ", vot = " ";
    var r1 = document.getElementById("GJ").checked;
    var r2 = document.getElementById("MH").checked;
    var r3 = document.getElementById("R").checked;
    if (r1 == true)
        reg = "Gujarat";
    else if (r2 == true)
        reg = "Maharashtra";
    else if (r3 == true)
        reg = "Rajasthan";
    if (reg != " ")
        f = 1;

    var b1 = document.getElementById("CEO").checked;
    var b2 = document.getElementById("CFO").checked;
    var b3 = document.getElementById("EC").checked;

    if (b1 == true)
        pso = "CEO";
    else if (b2 == true)
        pos = "CFO";
    else if (b3 == true)
        pos = "EC";
    if (pos != " ")
        f = 1;

    var s1 = document.getElementById("Age").checked;
    var s2 = document.getElementById("Gender").checked;
    var s3 = document.getElementById("Date").checked;

    if (s1 == true)
        vot = "Age";
    else if (s2 == true)
        vot = "Gender";
    else if (s3 == true)
        vot = "Date";
    if (vot != " ")
        f = 1;

    if (f == 1) {
        var result;
        var text = "";

        if (reg != " " && pos != " ") {
            result = JSON.parse(candidates).filter(function (entry) {
                return (entry.region === reg && entry.positon == pos);
            });
        } else if (reg != " ") {
            result = JSON.parse(candidates).filter(function (entry) {
                return (entry.region === reg);
            });
        } else {
            result = JSON.parse(candidates).filter(function (entry) {
                return (entry.position == pos);
            });
        }
        //console.log(result)
        for (var i = 0; i < result.length; i++) {
            var obj = result[i];
            text += "<h3>" + "Name: " + "<i>" + obj.name + "</i>" + "<br>" +
                "Position: " + "<i>" + obj.position + "</i>" + "<br>" +
                "Region: " + "<i>" + obj.region + "</i>" + "<br>" +
                "Votes: " + "<i>" + obj.votes + "</i>" + "<br>";
        }

        if (text != "")
            document.getElementById("print").innerHTML = text;
        else
            document.getElementById("print").innerHTML = "<h2 style= 'color:red;'>" + "<b>There is no product with such specs!!</b>" + "</h2>";

    }
    else
        document.getElementById("print").innerHTML = "<h2 style= 'color:red;'>" + "<b>There is no filter selected</b>" + "</h2>";
}