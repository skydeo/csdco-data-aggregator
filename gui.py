import timeit
from gooey import Gooey, GooeyParser
import mscl_aggregator as mst
import xyz_aggregator as mxyz
import xrf_aggregator as xrf


@Gooey(program_name='Data Aggregator',
       navigation='TABBED',
       default_size=(600, 600))
def main():
  parser = GooeyParser(description='Aggregate data from Geotek and _____ machine outputs.')

  subs = parser.add_subparsers(help='commands', dest='command')

  mst_parser = subs.add_parser('MSCL-S', help='Combine whole-core data.')
  input_output_mst = mst_parser.add_argument_group(gooey_options={'columns': 1})
  input_output_mst.add_argument('input_directory',
                                metavar='Input Directory',
                                type=str,
                                widget='DirChooser',
                                help='Directory containing the MSCL folders.')
  input_output_mst.add_argument('output_filename',
                                metavar='Output Filename',
                                type=str,
                                help='Name of the combined output file.')
  options_mst = mst_parser.add_argument_group('Options', gooey_options={'columns': 1})
  options_mst.add_argument('-e', '--excel',
                           metavar='Export as Excel',
                           action='store_true',
                           help='Export combined data as an Excel (xlsx) file.')
  options_mst.add_argument('-v', '--verbose',
                           metavar='Verbose',
                           action='store_true',
                           help='Display troubleshooting info.')

  xyz_parser = subs.add_parser('MSCL-XYZ', help='Combine split-core data.')

  xrf_parser = subs.add_parser('XRF', help='Combine XRF data.')
  input_output_xrf = xrf_parser.add_argument_group(gooey_options={'columns': 1})
  input_output_xrf.add_argument('input_directory',
                                metavar='Input Directory',
                                type=str,
                                widget='DirChooser',
                                help='Directory containing the XRF Excel files.')
  input_output_xrf.add_argument('output_filename',
                                metavar='Output Filename',
                                type=str,
                                help='Name of the combined output file.')
  options_xrf = xrf_parser.add_argument_group('Options', gooey_options={'columns': 1})
  options_xrf.add_argument('-e', '--excel',
                           metavar='Export as Excel',
                           action='store_true',
                           help='Export combined data as an Excel (xlsx) file.')
  options_xrf.add_argument('-v', '--verbose',
                           metavar='Verbose',
                           action='store_true',
                           help='Display troubleshooting info.')


  args = parser.parse_args()

  if args.command == 'MSCL-S':
    mst.aggregate_mscl_data(args.input_directory, args.output_filename, args.excel, args.verbose)
  elif args.command == 'MSCL-XYZ':
    print('Soon.')
  elif args.command == 'XRF':
    xrf.aggregate_xrf_data(args.input_directory, args.output_filename, args.excel, args.verbose)
  else:
    print(f"Something went wrong. Invalid data type: {args.data_type}")


if __name__ == '__main__':
  main()
