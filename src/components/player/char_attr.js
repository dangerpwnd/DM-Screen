import React from "react";

const charAttr = (props) => {

    const { str, dex, con, int, wis, cha} = props;

    return(
        <div className="playerAttrGrid">
            <div className="border">
                <h3>Str: {str}</h3>
                <h3>Dex: {dex}</h3>
                <h3>Con: {con}</h3>
                <h3>Int: {int}</h3>
                <h3>Wis: {wis}</h3>
                <h3>Cha: {cha}</h3>
            </div>
        </div>
    )
};

export default charAttr;