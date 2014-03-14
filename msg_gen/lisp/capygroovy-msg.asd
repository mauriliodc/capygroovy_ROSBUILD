
(cl:in-package :asdf)

(defsystem "capygroovy-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Ticks" :depends-on ("_package_Ticks"))
    (:file "_package_Ticks" :depends-on ("_package"))
  ))