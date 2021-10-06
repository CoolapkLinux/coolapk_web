import * as Base64 from 'base-64'
import md5 from 'md5'

export function get_token() {
	var DEVICE_ID = "8513efac-09ea-3709-b214-95b366f1a185"

	var t = Date.now()
	// 将时间戳截到10位再转16进制
	var hex_t = "0x"+Number(t.toFixed().substring(0, 10)).toString(16)
	var md5_t = md5(t.toFixed())
	var a = `token://com.coolapk.market/c67ef5943784d09750dcfbb31020f0ab?${md5_t}${DEVICE_ID}&com.coolapk.market`

	var md5_a = md5(Base64.encode(a))
	return `${md5_a}${DEVICE_ID}${hex_t}`
}

console.log(get_token())
