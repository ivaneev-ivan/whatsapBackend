import { Button, Flex, Input, Table, Textarea } from '@mantine/core'
import { FC, useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { getAllPhones } from '../api/api'
import { PhoneLimit } from '../api/types'
import Layout from '../components/Layout'

const GetRow: FC<PhoneLimit> = el => {
	const [data, setData] = useState<PhoneLimit>(el)
	return (
		<Table.Tr>
			<Table.Td>
				<Link to='#'>{data.id}</Link>
			</Table.Td>
			<Table.Td>
				<Flex gap='xs'>
					<Input
						onChange={e =>
							setData({
								...data,
								message_sec_limits_from: Number(e.target.value),
							})
						}
						value={data.message_sec_limits_from}
					/>
					<Input value={data.message_sec_limits_to} />
				</Flex>
			</Table.Td>
			<Table.Td>
				<Flex gap='xs'>
					<Input value={data.message_autoanswer_sec_limits_from} />
					<Input value={data.message_autoanswer_sec_limits_to} />
				</Flex>
			</Table.Td>
			<Table.Td>
				<Flex gap='xs'>
					<Input value={data.warming_message_sec_limits_from} />
					<Input value={data.warming_message_sec_limits_to} />
				</Flex>
			</Table.Td>
			<Table.Td>
				<Flex gap='xs'>
					<Input value={data.warming_call_outgoing_sec_limits_from} />
					<Input value={data.warming_call_outgoing_sec_limits_to} />
				</Flex>
			</Table.Td>
			<Table.Td>{data.phone.online ? 'Онлайн' : 'Офлайн'}</Table.Td>
			<Table.Td>
				<Textarea
					value={data.phone.device.note === null ? '' : data.phone.device.note}
				/>
			</Table.Td>
			<Table.Td>
				<Button variant='filled' color='red'>
					X
				</Button>
			</Table.Td>
		</Table.Tr>
	)
}

const Home = () => {
	const [data, setData] = useState<PhoneLimit[]>([])
	useEffect(() => {
		;(async () => {
			setData(await getAllPhones())
		})()
	}, [])

	return (
		<Layout>
			<Table highlightOnHover withTableBorder withColumnBorders>
				<Table.Thead>
					<Table.Tr>
						<Table.Th>Номер тел.</Table.Th>
						<Table.Th>Рассылка (лимиты)</Table.Th>
						<Table.Th>Автоответчик (лимиты)</Table.Th>
						<Table.Th>Прогрев сообщ. (лимиты на отпр.)</Table.Th>
						<Table.Th>Прогрев исх. звон.</Table.Th>
						<Table.Th>Статус того что делает телефон</Table.Th>
						<Table.Th>Примечание</Table.Th>
						<Table.Th></Table.Th>
					</Table.Tr>
				</Table.Thead>
				<Table.Tbody>
					{data.map(el => (
						<GetRow {...el} key={'phone limit ' + el.id} />
					))}
				</Table.Tbody>
			</Table>
		</Layout>
	)
}

export default Home
