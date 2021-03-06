import { useEffect } from "react";
import { useParams } from "react-router-dom";
import classes from "./CollDetails.module.css";

import Products from "./Products.js";

function CollDetails() {
  const params = useParams();

  // useEffect(() => {
  //   dispatch(fetchCollItems(params.collections));
  // }, [params.collections]);

  return (
    <>
      <h1 className={classes.header}>{params.collection}</h1>
      <Products />
    </>
  );
}
export default CollDetails;
