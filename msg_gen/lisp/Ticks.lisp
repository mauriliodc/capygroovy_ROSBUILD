; Auto-generated. Do not edit!


(cl:in-package capygroovy-msg)


;//! \htmlinclude Ticks.msg.html

(cl:defclass <Ticks> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (leftTick
    :reader leftTick
    :initarg :leftTick
    :type cl:integer
    :initform 0)
   (rightTick
    :reader rightTick
    :initarg :rightTick
    :type cl:integer
    :initform 0))
)

(cl:defclass Ticks (<Ticks>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Ticks>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Ticks)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name capygroovy-msg:<Ticks> is deprecated: use capygroovy-msg:Ticks instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Ticks>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader capygroovy-msg:header-val is deprecated.  Use capygroovy-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'leftTick-val :lambda-list '(m))
(cl:defmethod leftTick-val ((m <Ticks>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader capygroovy-msg:leftTick-val is deprecated.  Use capygroovy-msg:leftTick instead.")
  (leftTick m))

(cl:ensure-generic-function 'rightTick-val :lambda-list '(m))
(cl:defmethod rightTick-val ((m <Ticks>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader capygroovy-msg:rightTick-val is deprecated.  Use capygroovy-msg:rightTick instead.")
  (rightTick m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Ticks>) ostream)
  "Serializes a message object of type '<Ticks>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'leftTick)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'rightTick)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Ticks>) istream)
  "Deserializes a message object of type '<Ticks>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'leftTick) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rightTick) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Ticks>)))
  "Returns string type for a message object of type '<Ticks>"
  "capygroovy/Ticks")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Ticks)))
  "Returns string type for a message object of type 'Ticks"
  "capygroovy/Ticks")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Ticks>)))
  "Returns md5sum for a message object of type '<Ticks>"
  "9e343431b3b11d8350b35ecbcfc68da9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Ticks)))
  "Returns md5sum for a message object of type 'Ticks"
  "9e343431b3b11d8350b35ecbcfc68da9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Ticks>)))
  "Returns full string definition for message of type '<Ticks>"
  (cl:format cl:nil "Header header~%int32 leftTick~%int32 rightTick~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Ticks)))
  "Returns full string definition for message of type 'Ticks"
  (cl:format cl:nil "Header header~%int32 leftTick~%int32 rightTick~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Ticks>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Ticks>))
  "Converts a ROS message object to a list"
  (cl:list 'Ticks
    (cl:cons ':header (header msg))
    (cl:cons ':leftTick (leftTick msg))
    (cl:cons ':rightTick (rightTick msg))
))
