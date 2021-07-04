import React from "react";

const charModifier = (props) => {

    const { profBonus, attrMod, attrSave} = props;

    return(
        <div className="playerModGrid">
            <div className="border playerFlexRow">
                <h3>Prof Bonus: {profBonus}</h3>
                <h3>Attr Modifier: {attrMod}</h3>
                <h3>Attr Save: {attrSave}</h3>
            </div>
        </div>
    )
};

export default charModifier;