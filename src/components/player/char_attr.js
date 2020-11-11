import React from "react";

const charAttr = (props) => {
    return(
        <div className="playerAttrGrid">
            <div className="border">
                <h3>Str: {props.attr.str}</h3>
                <h3>Dex: {props.attr.dex}</h3>
                <h3>Con: {props.attr.con}</h3>
                <h3>Int: {props.attr.int}</h3>
                <h3>Wis: {props.attr.wis}</h3>
                <h3>Cha: {props.attr.cha}</h3>
            </div>
        </div>
    )
};

export default charAttr;