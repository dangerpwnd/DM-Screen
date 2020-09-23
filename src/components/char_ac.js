import React from "react";

const charAc = (props) => {
    return(
        <div>
            <div className="border playerFlexRow">
                <h3>Regular: {props.base}</h3>
                <h3>Flat-footed: 13</h3>
                <h3>Touch: 12</h3>
            </div>
        </div>
    )
};

export default charAc;