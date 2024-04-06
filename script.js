const sqlite3 = require('sqlite3').verbose();
let sql;

const db = new sqlite3.Database('./importCSVtoSQLite/customer.db', sqlite3.OPEN_READWRITE, (err) => {
    if (err) return console.error(err.message);
})


sql = 'SELECT * FROM customer WHERE country="Netherlands"';

// db.all(sql, [], (err, rows) => {
//     if (err) return console.error(err.message);
//     rows.forEach(row => {
//         console.log(row);
//     });
// });

db.each(sql, [], (err, row) => {
    if (err) return console.error(err.message);
    // document.getElementById("main").innerHTML(row.first_name);
    console.log(row);
});

// db.get(sql, [], (err, rows) => {
//     if (err) return console.error(err.message);
//     console.log(rows);
// });