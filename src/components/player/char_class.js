import React from "react";

const charClass = (props) => {

    const {name, level} = props;

    return(
        <div>
            <div className="border playerFlexRow">
                <h2>{name}</h2>
                <h2>{level}</h2>
            </div>
        </div>
    )
};

export default charClass;