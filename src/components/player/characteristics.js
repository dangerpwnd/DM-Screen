import React from "react";

const characteristics = (props) => {

    const {eyes, hair, height, weight, bond, flaw } = props;

    return(
        <div className="playerCharGrid playerFlexCol">
            <div className="border">
                <h3>Eyes: {eyes}</h3>
                <h3>Hair: {hair}</h3>
                <h3>Height: {height}</h3>
                <h3>Weight: {weight}</h3>
                <h3>Bond: {bond}</h3>
                <h3>Flaw: {flaw}</h3>
            </div>
        </div>
    )
};

export default characteristics;