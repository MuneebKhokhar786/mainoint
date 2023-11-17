import axios from "axios";

const handleRequest = (uurl) => {
  return axios({
    url: uurl,
    method: "GET",
    headers: {
      Accept: "application/json",
    },
  });
};

export default handleRequest;
