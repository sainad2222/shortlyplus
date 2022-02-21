import axios from "axios";
import React, { useState } from "react";
import { Button, Form, Spinner } from "react-bootstrap";
import "./index.css";

function App() {
  const [term, setTerm] = useState("");
  const [toggle, setToggle] = useState(1);
  const [slug, setSlug] = useState("");
  const [short, setShort] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(0);

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
      setTerm("");
      setSlug("");
      setShort(serverURL+"/"+res.data.shortURL);
      setError("");
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
    </div>
  );
}

export default App;
