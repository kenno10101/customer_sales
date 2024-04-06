const sqlite3 = require('sqlite3').verbose();
let sql;

const db = new sqlite3.Database('./importCSVtoSQLite/customer.db', sqlite3.OPEN_READWRITE, (err) => {
    if (err) return console.error(err.message);
})


sql = 'SELECT * FROM customer WHERE country="Netherlands"';

var first_names = [];
var testname;

// db.all(sql, [], (err, rows) => {
//     if (err) return console.error(err.message);
//     rows.forEach(row => {
//         console.log(row);
//     });
// });

db.each(sql, [], (err, row) => {
    if (err) return console.error(err.message);
    // document.getElementById("main").innerHTML(row.first_name);
    first_names.push(row.first_name);
    testname = row.first_name;
    // console.log(typeof row.first_name);
});

// db.get(sql, [], (err, rows) => {
//     if (err) return console.error(err.message);
//     console.log(rows);
// });

console.log(first_names);
console.log(testname);