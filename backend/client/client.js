const express = require("express")
const { shortenerClient, dbClient } = require("./grpc")
const bodyParser = require("body-parser")

const app = express()

app.use(bodyParser.json())
app.post('/', async (req, res) => {
    await shortenerClient.shortenURL(req.body, (err, result) => {
        if (err) {
            console.log("[ERROR]", err)
            return res.json(err)
        }
        resErr = result.error
        if (resErr) {
            console.log("[ERROR]", resErr)
            return res.json(resErr)
        }
        res.json(result)
    })
})

app.get('/:slug', async (req, res) => {
    await dbClient.fetchURLFromSlug({ "slug": req.params.slug }, (err, result) => {
        if (err) {
            console.log("[ERROR]", err)
            return res.json(err)
        }
        resErr = result.error
        if (resErr) {
            console.log("[ERROR]", resErr)
            return res.json(resErr)
        }
        res.redirect(result.URL)
    })
})

const PORT = 8084
app.listen(PORT, () => {
    console.log(`[INFO] server running on port ${PORT}`)
})
