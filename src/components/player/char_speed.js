import React from "react";

const charSpeed = (props) => {

    const { speed, initiative } = props;

    return(
        <div>
            <div className="border playerFlexRow">
                <h3>Speed: {speed}</h3>
                <h3>Initiative: {initiative}</h3>
            </div>
        </div>
    )
};

export default charSpeed;