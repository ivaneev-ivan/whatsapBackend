export interface PhoneLimit {
	id: number
	phone: Phone
	warming_call_outgoing_sec_limits_from: number
	warming_call_outgoing_sec_limits_to: number
	warming_call_outgoing_sec_limits_delta: number
	warming_call_outgoing_sec_limits_from_min: number
	warming_call_outgoing_sec_limits_to_min: number
	warming_call_outgoing_duration_sec_limits_from: number
	warming_call_outgoing_duration_sec_limits_to: number
	warming_call_incoming_take_phone_sec_limits_from: number
	warming_call_qty_outgoing: number
	warming_call_qty_incoming: number
	warming_message_sec_limits_from: number
	warming_message_sec_limits_to: number
	warming_message_sec_limits_delta: number
	warming_message_sec_limits_from_min: number
	warming_message_sec_limits_to_min: number
	warming_message_qty_sent: number
	warming_message_qty_receive: number
	message_sec_limits_from: number
	message_sec_limits_to: number
	message_autoanswer_sec_limits_from: number
	message_autoanswer_sec_limits_to: number
}

export interface Phone {
	id: number
	device: Device
	phone: string
	online: boolean
	wa_is_business: boolean
}

export interface Device {
	id: number
	serial: string
	model: string
	note: string | null
}
