import React from "react";
import charClass from "./char_class";
import charSpeed from "./char_speed";
import charAc from "./char_ac";

const charMain = (props) => {
    return(
            <div className="playerMainGrid">
                    <h1 className="border">Bartos Donadarion</h1>
                    <charClass />
                    <charSpeed />
                    <charAc base={props.ac.base} />
            </div>
    )
};

export default charMain;