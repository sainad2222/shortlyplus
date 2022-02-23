import axios from "axios";
import React, { useState, useRef, useEffect } from "react";
import { Button, Form, Spinner } from "react-bootstrap";
import "./index.css";

function App() {
    const [term, setTerm] = useState("");
    const [toggle, setToggle] = useState(1);
    const [slug, setSlug] = useState("");
    const [short, setShort] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(0);
    const [urls, setUrls] = useState([]);

    const mounted = useRef();
    useEffect(() => {
        if (!mounted.current) {
            // do componentDidMount logic
            var Urls = localStorage.getItem("urls")
            if (Urls) {
                setUrls(JSON.parse(Urls))
            }
            mounted.current = true;
        } else {
            // do componentDidUpdate logic
            localStorage.setItem("urls", JSON.stringify(urls))
        }
    }, [urls]);

    const handleSubmit = async (event) => {
        event.preventDefault();
        setLoading(1);
        var req;
        if (slug !== "") {
            req = {
                url: term,
                slug: slug,
            };
        } else {
            req = {
                url: term,
            };
        }
        const serverURL = process.env.REACT_APP_SERVER || "http://localhost:8084"
        try {
            const res = await axios.post(serverURL, req);
            if (!res.data.shortURL) {
                setError(res.data);
                setShort("");
            }
            else {
                setTerm("");
                setSlug("");
                const shorty = serverURL + "/" + res.data.shortURL
                setShort(shorty);
                setError("");
                var newUrls = [...urls, { shortURL: shorty }]
                setUrls(newUrls)
            }
        } catch (err) {
            console.log(err);
            setError("Cannot make request to backend");
            setShort("");
        }
        setLoading(0);
    };

    const handleChange = (event) => {
        setTerm(event.target.value);
    };

    const handleSlugChange = (event) => {
        setSlug(event.target.value);
    };

    const handleToggle = (event) => {
        setToggle(!toggle);
    };

    const handleClear = (event) => {
        setUrls([])
    }

    const renderShort = () => {
        if (short !== "") {
            return (
                <div className="message">
                    <h4>
                        Short link: <a href={short} target="_blank" rel="noopener noreferrer">{short}</a>
                    </h4>
                </div>
            );
        }
    };

    const renderSpinner = () => {
        if (loading) {
            return (
                <div className="spinners">
                    <Spinner animation="grow" variant="primary" />
                    <Spinner animation="grow" variant="primary" />
                    <Spinner animation="grow" variant="primary" />
                </div>
            );
        }
    };

    const renderError = () => {
        if (error !== "") {
            return (
                <div className="message">
                    <h4>
                        Error: <span className="error">{error}</span>
                    </h4>
                </div>
            );
        }
    };

    const renderURLS = () => {
        console.log(urls)
        if (urls.length === 0) {
            return <div></div>
        }
        var urlsList = urls.map(function (url, index) {
            return <tr><th scope="row"><td><a href={url.shortURL} target="_blank" rel="noopener noreferrer">{url.shortURL}</a></td></th></tr>;
        })
        return (
            <table className="table">
                <thead>
                    <tr>
                        <th scope="col">History: <Button variant="danger" onClick={handleClear}>clear</Button></th>
                    </tr>
                </thead>
                <tbody>
                    {urlsList}
                </tbody>
            </table>
        )
    }

    const renderSlug = () => {
        if (toggle) {
            return (
                <div>
                    <Button variant="success" onClick={handleToggle} active>
                        Random
                    </Button>{" "}
                    <Button variant="info" onClick={handleToggle}>
                        Custom
                    </Button>
                </div>
            );
        } else {
            return (
                <div>
                    <Button variant="success" onClick={handleToggle}>
                        Random
                    </Button>{" "}
                    <Button variant="info" onClick={handleToggle} active>
                        Custom
                    </Button>
                    <Form.Control
                        className="input"
                        value={slug}
                        onChange={handleSlugChange}
                        placeholder="Enter custom short name for your url"
                    />
                </div>
            );
        }
    };

    return (
        <div className="container">
            <Form className="form" onSubmit={handleSubmit}>
                <Form.Group>
                    <Form.Label className="label">URL</Form.Label>
                    <Form.Control
                        className="input"
                        value={term}
                        onChange={handleChange}
                        placeholder="Enter Url"
                    />
                </Form.Group>
                <Form.Group>
                    <Form.Label className="label">Short Name</Form.Label>
                    {renderSlug()}
                </Form.Group>
                <Button variant="primary" type="submit" className="shortify">
                    Shortify
                </Button>
            </Form>
            {renderSpinner()}
            {renderShort()}
            {renderError()}
            {renderURLS()}
        </div>
    );
}

export default App;
