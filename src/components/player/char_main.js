import React from "react";
import CharClass from "./char_class";
import CharSpeed from "./char_speed";
import CharAc from "./char_ac";

const charMain = (props) => {

        const ac = props.ac;
        const charClass = props.char_class;

    return(
            <div className="playerMainGrid">
                    <h1 className="border">Bartos Donadarion</h1>
                    <CharClass class_name={charClass.class_name} level={charClass.level} />
                    <CharSpeed  class_speed={charClass.class_speed} />
                    <CharAc ac={ac} />
            </div>
    )
};

export default charMain;