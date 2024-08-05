import axios from 'axios'
import { PhoneLimit } from './types'

export const getAllPhones = async () => {
	const response = await axios.get('http://localhost/api/phones_limits')
	if (response.status === 200) {
		return response.data as PhoneLimit[]
	}
	return []
}
