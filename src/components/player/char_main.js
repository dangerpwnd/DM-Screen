import React from "react";
import CharClass from "./char_class";
import CharAc from "./char_ac";
import Speed from "./char_speed";

const charMain = (props) => {

        const { charName } = props;

    return(
            <div className="playerMainGrid">
                    <h1 className="border">{charName}</h1>
                    <CharClass  />
                    <Speed  />
                    <CharAc />
            </div>
    )
};

export default charMain;