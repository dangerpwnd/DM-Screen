import React from "react";
import CharClass from "./char_class";
import CharSpeed from "./char_speed";
import CharAc from "./char_ac";

const charMain = (props) => {
    return(
            <div className="playerMainGrid">
                    <h1 className="border">Bartos Donadarion</h1>
                    <CharClass />
                    <CharSpeed />
                    <CharAc ac={props.ac} />
            </div>
    )
};

export default charMain;