const express = require("express")
const client = require("./grpc")
const bodyParser = require("body-parser")

const app = express()

app.use(bodyParser.json())
app.post('/', (req, res) => {
    client.shortenURL(req.body, (err, result) => {
        if (err) {
            console.log("[ERROR]", err)
            res.json(err)
        }
        res.json(result)
    })
})

const PORT = 8084
app.listen(PORT, () => {
    console.log(`[INFO] server running on port ${PORT}`)
})
